#!coding=utf-8
import json
import math
import genre_recommender
import mawid_recommender





def generate_user_preference_vector(list_user_liked_movie_id, dic_id_with_genre):
    
    list_of_liked_movie_genre_vector = []

    for id in list_user_liked_movie_id:
        try:
            list_of_liked_movie_genre_vector.append(dic_id_with_genre[id])
        except KeyError:
            continue

    user_preference_vector = reduce(lambda x, y: [m + n for m, n in zip(x, y)], list_of_liked_movie_genre_vector)
    print 'user_preference_vector: ', user_preference_vector

    return user_preference_vector


def generate_user_mawid_preference_dic(user_liked_movie_id_list, dic_id_with_mawid):
    user_mawid_preference_dic = {}

    user_mawid_list = []

    for movie_id in user_liked_movie_id_list:
        try:
            user_mawid_list += dic_id_with_mawid[movie_id]
        except KeyError:
            continue

    user_mawid_set_list = list(set(user_mawid_list))

    for item in user_mawid_set_list:
        user_mawid_preference_dic[item] = user_mawid_list.count(item)

    return user_mawid_preference_dic


def get_sum_of_all_mawid_in_all_movies(dic_id_with_mawid):

    mawid_list = dic_id_with_mawid.values()
    result = sum(map(lambda x: len(x), mawid_list))
    print 'sum_of_all_mawid_in_all_movies:',result
    return result


def get_sum_of_every_mawid_dic(mawid_with_count_file):
    mawid_with_count_file = open(mawid_with_count_file)
    content = json.loads(mawid_with_count_file.readline())

    return content

###########################################################################

################################################################################
# 为genre推荐的前期处理
file_my_liked_movie_list = open("my_liked_movie_list.txt")
list_user_liked_movie_id = []
for line_of_my_liked_movie_list in file_my_liked_movie_list:
    list_user_liked_movie_id.append(line_of_my_liked_movie_list.strip())
print list_user_liked_movie_id


file_movie_genre_vector = open('movie_genre_vector.json')
dic_id_with_genre = json.loads(file_movie_genre_vector.readline())

user_preference_vector = generate_user_preference_vector(list_user_liked_movie_id, dic_id_with_genre)

genre_cos_sim_dic = genre_recommender.recommend(user_preference_vector, dic_id_with_genre)

##########################################################################################
# 为mawid推荐的前期处理
my_liked_movie_list_file = open("mark_liked_movie_id.txt")
user_liked_movie_id_list = []
for line in my_liked_movie_list_file:
    user_liked_movie_id_list.append(line.strip())
print 'user_liked_movie_id_list:', user_liked_movie_id_list


movie_id_with_mawid_file = open('movie_id_with_mawid.json')
dic_id_with_mawid = json.loads(movie_id_with_mawid_file.readline())


user_mawid_preference_dic = generate_user_mawid_preference_dic(user_liked_movie_id_list, dic_id_with_mawid)

# 此值在外部算好，避免进入循环增大计算量
sum_of_all_mawid_in_all_movies = get_sum_of_all_mawid_in_all_movies(dic_id_with_mawid)
# generate_sum_of_every_mawid_dic(dic_id_with_mawid) 
sum_of_every_mawid_dic = get_sum_of_every_mawid_dic('mawid_with_count.json')




mawid_cos_sim_dic = mawid_recommender.recommend(user_mawid_preference_dic, dic_id_with_mawid, sum_of_all_mawid_in_all_movies, sum_of_every_mawid_dic)