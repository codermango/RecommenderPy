#!coding=utf-8
from __future__ import division
import json




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


def get_sum_of_every_mawid_dic(dic_id_with_mawid):   # 太耗时！！！！！！！！！！
    mawid_list = []
    dic_id_with_mawid_values = dic_id_with_mawid.values()
    mawid_list = reduce(lambda x, y: x + y, dic_id_with_mawid_values)
    mawid_list = set(mawid_list)

    mawid_with_count_dic = {}
    num = 0
    for item in mawid_list:
        num += reduce(lambda x, y: x.count(item) + y.count(item), dic_id_with_mawid_values)
        print num, 'bbb'
        break

    print len(mawid_list), 'aaaaa'


def get_cos_sim(user_mawid_preference_dic, mawid_list, sum_of_all_mawid_in_all_movies):

    # 首先把两个列表的元素组合在一起
    values_of_user_mawid_preference_dic = user_mawid_preference_dic.values()
    difference_list = list(set(mawid_list).difference(set(values_of_user_mawid_preference_dic)))

    map(lambda x: user_mawid_preference_dic.setdefault(x, 0), difference_list)

    sum_of_every_mawid_dic = {}

    # 然后算出tf-idf
    sum_of_user_liked_mawid = sum(user_mawid_preference_dic.values())
    print sum_of_user_liked_mawid
    tf_dic = {}
    for k, v in user_mawid_preference_dic.items():
        tf_dic[k] = v / sum_of_user_liked_mawid

    print tf_dic

    idf_dic = {}
    
    #最后算出cos相似度

  
    


    



def recommend(user_mawid_preference_dic, num_of_recommended_movies, dic_id_with_mawid, sum_of_all_mawid_in_all_movies):

    for k, v in dic_id_with_mawid.items():
        mawid_list = v
        cos_sim = get_cos_sim(user_mawid_preference_dic, mawid_list, sum_of_all_mawid_in_all_movies)
        break

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
sum_of_every_mawid_dic = get_sum_of_every_mawid_dic(dic_id_with_mawid)

recommended_movie_id = recommend(user_mawid_preference_dic, num_of_recommended_movies, dic_id_with_mawid, sum_of_all_mawid_in_all_movies)












