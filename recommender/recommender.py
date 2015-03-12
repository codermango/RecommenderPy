#!coding=utf-8

import json

####################################################################################################






def get_sum_of_all_genre_in_liked_movies(list_user_liked_movie_id, file_movie_genre_vector):
    num_of_genre = 0
    file_movie_genre_vector = open(file_movie_genre_vector)
    dic_id_with_genre = json.loads(file_movie_genre_vector.readline())

    count = 0
    for id in list_user_liked_movie_id:
    	try:
        	list_genre_vector = dic_id_with_genre[id]
        except KeyError:
        	continue
        # 获取list_genre_vector中1的个数，即为此id的genre数
        count += list_genre_vector.count(1)
    print count
     





#####################################################################################################

f_my_liked_movie_list = open("my_liked_movie_list.txt")
list_user_liked_movie_id = []

for line_of_my_liked_movie_list in f_my_liked_movie_list:
    list_user_liked_movie_id.append(line_of_my_liked_movie_list.strip())

print list_user_liked_movie_id

num_of_recommended_movies = 20

sum_of_all_genre_in_liked_movies = get_sum_of_all_genre_in_liked_movies(list_user_liked_movie_id, 'movie_genre_vector.json')
print sum_of_all_genre_in_liked_movies



