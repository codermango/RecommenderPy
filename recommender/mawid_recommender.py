#!coding=utf-8
from __future__ import division
import json
import math



def generate_user_mawid_preference_dic(user_liked_movie_id_list, dic_id_with_mawid):
    user_mawid_preference_dic = {}

    user_mawid_list = []

    for movie_id in user_liked_movie_id_list:
        try:
            user_mawid_list += dic_id_with_mawid[movie_id]
        except KeyError:
            continue

    user_mawid_set = set(user_mawid_list)

    for item in user_mawid_set:
        user_mawid_preference_dic[item] = user_mawid_list.count(item)

    print user_mawid_preference_dic
    return user_mawid_preference_dic



def get_sum_of_all_mawid_in_all_movies(dic_id_with_mawid):

    mawid_list = dic_id_with_mawid.values()
    result = sum(map(lambda x: len(x), mawid_list))
    print 'sum_of_all_mawid_in_all_movies:',result
    return result


def generate_sum_of_every_mawid_dic(dic_id_with_mawid):   # 太耗时！！！！！！！！！！
    mawid_list = []
    dic_id_with_mawid_values = dic_id_with_mawid.values()
    mawid_list = reduce(lambda x, y: x + y, dic_id_with_mawid_values)
    mawid_list = list(set(mawid_list))

    print len(mawid_list)
    print len(dic_id_with_mawid), 'aaa'

    mawid_with_count_dic = {}
    for mawid in mawid_list:
        num = 0
        for k, v in dic_id_with_mawid.items():
            num += v.count(mawid)
        mawid_with_count_dic[mawid] = num
        print 0

    mawid_with_count_file = open('mawid_with_count.json', 'w')
    mawid_with_count_json = json.dumps(mawid_with_count_dic)
    mawid_with_count_file.write(mawid_with_count_json + "\n")

    mawid_with_count_file.close()

    print len(mawid_with_count_dic)




def get_sum_of_every_mawid_dic(mawid_with_count_file):
    mawid_with_count_file = open(mawid_with_count_file)
    content = json.loads(mawid_with_count_file.readline())
    print len(content), 'aaa'
    print content['405166']
    return content


def get_cos_sim(user_mawid_preference_dic, mawid_list, sum_of_all_mawid_in_all_movies, sum_of_every_mawid_dic):

    values_of_user_mawid_preference_dic = user_mawid_preference_dic.values()

    # 首先把两个列表的元素组合在一起
    difference_list = list(set(mawid_list).difference(set(values_of_user_mawid_preference_dic)))

    map(lambda x: user_mawid_preference_dic.update({x: 0}), difference_list)
    
    mawid_list_dic = {}
    map(lambda x: mawid_list_dic.update({x: 0}), user_mawid_preference_dic.keys())

    # print mawid_list_dic.values()

    map(lambda x: mawid_list_dic.update({x: 1}), mawid_list)

    # print mawid_list_dic.values()



    # 然后算出tf-idf
    sum_of_user_liked_mawid = sum(user_mawid_preference_dic.values())
    # print sum_of_user_liked_mawid
    tf_dic = {}
    for k, v in user_mawid_preference_dic.items():
        tf_dic[k] = v / sum_of_user_liked_mawid

    # print 'tf_idc:', tf_dic

    idf_dic = {}
    for i, j in user_mawid_preference_dic.items():
        idf_dic[i] = sum_of_all_mawid_in_all_movies / sum_of_every_mawid_dic[i]
    # print 'idf_dic:', idf_dic

    tfidf_dic = {}
    for key in tf_dic.keys():
        tfidf_dic[key] = tf_dic[key] * idf_dic[key]
    # print 'tfidf_dic:', tfidf_dic

    #最后算出cos相似度
    mawid_list_dic_value = mawid_list_dic.values()
    tfidf_dic_value = tfidf_dic.values()

    num1 = sum([x * y for x, y in zip(mawid_list_dic_value, tfidf_dic_value)])
    tmp1 = math.sqrt(sum([x ** 2 for x in mawid_list_dic_value]))
    tmp2 = math.sqrt(sum([x ** 2 for x in tfidf_dic_value]))
    num2 = tmp1 * tmp2  # num2=sqrt(a1^2+a2^2+a3^2) * sqrt(b1^2+b2^2+b3^2)
    cos_value = num1 / num2
    print cos_value
    return cos_value



def recommend(user_mawid_preference_dic, num_of_recommended_movies, dic_id_with_mawid, sum_of_all_mawid_in_all_movies, sum_of_every_mawid_dic):

    values_of_user_mawid_preference_dic = user_mawid_preference_dic.values()
    cos_value_dic = {}
    for k, v in dic_id_with_mawid.items():
        mawid_list = v
        intersection_list = list(set(mawid_list).intersection(set(values_of_user_mawid_preference_dic)))

        if intersection_list:
            print intersection_list
            break

        cos_sim = get_cos_sim(user_mawid_preference_dic, mawid_list, sum_of_all_mawid_in_all_movies, sum_of_every_mawid_dic)

        cos_value_dic[k] = cos_sim
        print cos_sim, 'dd'

    print len(cos_value_dic)

###################################################################################################

my_liked_movie_list_file = open("myfavorite_chang.txt")
user_liked_movie_id_list = []
for line in my_liked_movie_list_file:
    user_liked_movie_id_list.append(line.strip())
print 'user_liked_movie_id_list:', user_liked_movie_id_list


movie_id_with_mawid_file = open('movie_id_with_mawid.json')
dic_id_with_mawid = json.loads(movie_id_with_mawid_file.readline())


num_of_recommended_movies = 20
user_mawid_preference_dic = generate_user_mawid_preference_dic(user_liked_movie_id_list, dic_id_with_mawid)

# 此值在外部算好，避免进入循环增大计算量
sum_of_all_mawid_in_all_movies = get_sum_of_all_mawid_in_all_movies(dic_id_with_mawid)
# generate_sum_of_every_mawid_dic(dic_id_with_mawid) 
sum_of_every_mawid_dic = get_sum_of_every_mawid_dic('mawid_with_count.json')




recommended_movie_id = recommend(user_mawid_preference_dic, num_of_recommended_movies, dic_id_with_mawid, sum_of_all_mawid_in_all_movies, sum_of_every_mawid_dic)












