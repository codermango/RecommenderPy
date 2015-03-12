#!coding=utf-8

import json

####################################################################################################






def get_sum_of_all_genre_in_liked_movies(list_user_liked_movie_id, file_movie_genre_vector):
    num_of_genre = 0
    file_movie_genre_vector = open(file_movie_genre_vector)
    dic_id_with_genre = json.loads(file_movie_genre_vector.readline())

    for id in list_user_liked_movie_id:
        list_genre_vector = dic_id_with_genre[id]





#####################################################################################################

f_my_liked_movie_list = open("my_liked_movie_list.txt")
list_user_liked_movie_id = []

for line_of_my_liked_movie_list in f_my_liked_movie_list:
    list_user_liked_movie_id.append(line_of_my_liked_movie_list.strip())

print list_user_liked_movie_id

num_of_recommended_movies = 20

sum_of_all_genre_in_liked_movies = get_sum_of_all_genre_in_liked_movies(list_user_liked_movie_id, 'movie_genre_vector.json')
print sum_of_all_genre_in_liked_movies



