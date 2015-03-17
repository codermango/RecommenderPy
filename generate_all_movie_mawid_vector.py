#!coding=utf-8
import json



def delete_empty_credits_and_crew(saved_file):
    tagdb_file = open('!tagdb.json')

    saved_file = open(saved_file, 'w')
    count = 0
    for line in tagdb_file:
        movie = json.loads(line)
        credits = movie['credits']

        if not credits:
            continue
        try:
            crew = movie['credits']['crew']
        except KeyError:
            continue
        movie_json = json.dumps(movie)
        saved_file.write(movie_json + '\n')
    saved_file.close()
    tagdb_file.close()
    print count




def get_id_with_crew(saved_file):
    after_delete_empty_credits_and_crew_file = open('1_after_delete_empty_credits_and_crew_file.json')

    id_with_crew_file = open(saved_file, 'w')

    count = 0
    for line in after_delete_empty_credits_and_crew_file:

        movie = json.loads(line)

        crew = movie['credits']['crew']

        try:
            imdb_id = movie['externalIds']['imdbId']
        except KeyError:
            continue

        movie_dic = dict()
        movie_dic['imdbId'] = imdb_id 
        movie_dic['crew'] = crew

        movie_json = json.dumps(movie_dic)
        id_with_crew_file.write(movie_json + '\n')

    id_with_crew_file.close()
    after_delete_empty_credits_and_crew_file.close()




def get_all_mawid(saved_file):
    tagdb_after_neaten_genres_file = open('tagdb_after_neaten_genres.json')

    mawid_list = []

    for line in tagdb_after_neaten_genres_file:
        movie = json.loads(line)
        mawid = movie['mawid']

        tmp_list = list(set(mawid).difference(set(mawid_list)))
        mawid_list += tmp_list

    mawid_list_file = open(saved_file, 'w')

    map(lambda x: mawid_list_file.write(x + '\n'), sorted(mawid_list))

    return sorted(mawid_list)


def generate_mawid_vector_json_file(saved_file, sorted_mawid_list):
    mawid_dic = dict()
    for i in range(0, len(sorted_mawid_list)):
        mawid_dic[sorted_mawid_list[i]] = i 

    tagdb_after_neaten_genres_file = open('tagdb_after_neaten_genres.json')
    movie_mawid_vector_file = open(saved_file, 'w')

    new_movie_dic = dict()
    for line in tagdb_after_neaten_genres_file:
        movie_mawid_vector = [0 for x in range(0, len(sorted_mawid_list))]

        print len(movie_mawid_vector)

        movie = json.loads(line)
        mawid = movie['mawid']
        imdb_id = movie['ids']['imdbId']

        for k in mawid:
            movie_mawid_vector[mawid_dic[k]] = 1
        new_movie_dic[imdb_id] = movie_mawid_vector


    new_movie_json = json.dumps(new_movie_dic)

    movie_mawid_vector_file.write(new_movie_json + '\n')

    tagdb_after_neaten_genres_file.close()
    movie_mawid_vector_file.close()




def generate_id_with_mawid_file(id_with_mawid_file):
    tagdb_after_neaten_genres_file = open('tagdb_after_neaten_genres.json')
    id_with_mawid_file = open(id_with_mawid_file, 'w')

    new_movie_dic = dict()
    for line in tagdb_after_neaten_genres_file:
        movie = json.loads(line)
        imdb_id = movie['ids']['imdbId']
        mawid = movie['mawid']

        new_movie_dic[imdb_id] = mawid

    movie_json = json.dumps(new_movie_dic)
    id_with_mawid_file.write(movie_json + '\n')

    tagdb_after_neaten_genres_file.close()
    id_with_mawid_file.close()
    



##########################################################################

#delete_empty_credits_and_crew('1_after_delete_empty_credits_and_crew_file.json')

# get_id_with_crew('2_id_with_crew_file.json')

# sorted_mawid_list = get_all_mawid('mawid_list.txt')

# generate_mawid_vector_json_file('movie_mawid_vector.json', sorted_mawid_list)

generate_id_with_mawid_file('movie_id_with_mawid.json')