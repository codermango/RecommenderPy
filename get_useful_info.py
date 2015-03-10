#!coding=utf-8
import json

######################################################################
# help function

def __handle_country_link_for_ids_info(country):
    country_list = []

    for item in country:
        if item.startswith('http'):
            pos = item.rfind('/')
            country_tmp = item[pos + 1: len(item)]
            country1 = country_tmp.replace('_', ' ')
            country_list.append(country1)
        else:
            country_list.append(item)
            
    return country_list

def __handle_language_link_for_ids_info(language):
    language_list = []

    for item in language:
        if item.startswith('http'):
            pos = item.rfind('/')
            language_tmp = item[pos + 1: len(item)]
            pos_of_underline = language_tmp.find('_')
            
            language1 = language_tmp[0: pos_of_underline]
            language_list.append(language1)
        else:
            language_list.append(item)

    return language_list


def get_tidy_ids(file_path):
    f_ids_info = open('!ids_info.json')
    f_tidy_ids = open(file_path, 'w')

    for line in f_ids_info:
        movie = json.loads(line)
        info = movie['info']
        language = info['language']
        country = info['country']

        mawid1 = info['mawid1']
        mawid2 = info['mawid2']
        mawid = list(set(mawid1).union(set(mawid2)))
        #print mawid
        if not mawid:
            continue

        country = __handle_country_link_for_ids_info(country)
        language = __handle_language_link_for_ids_info(language)

        ids = movie['ids']
        for id in ids.keys():
            if id == 'freebase_id':
                ids['freebaseId'] = ids[id]
                del ids['freebase_id']
            elif id == 'wiki_page_id':
                ids['wikipediaPageId'] = ids[id]
                del ids['wiki_page_id']
            elif id == 'imdb_id':
                ids['imdbId'] = ids[id]
                del ids['imdb_id']
            elif id == 'rottentomatoes_id':
                del ids['rottentomatoes_id']
            elif id == 'netflix_id':
                del ids['netflix_id']
        #print ids

        info_dic = dict()
        info_dic['mawid'] = mawid
        #print mawid
        info_dic['language'] = language
        info_dic['country'] = country

        #print info_dic

        movie_dic = dict()
        movie_dic["info"] = info_dic
        movie_dic['ids'] = ids

        #print movie_dic

        movie_json = json.dumps(movie_dic)
        f_tidy_ids.write(movie_json+'\n')
    f_tidy_ids.close()



def __handle_language_for_tagdb(language):
    language_list = []
    count = 0
    for item in language:
        language_list.append(item['name'])
    return language_list

def __handle_genres_for_tagdb(genres):
    genres_list = []
    for item in genres:
        genres_list.append(item['name'])
    return genres_list




def delete_unusefull_info(file_path):
    f_tagdb = open('!tagdb.json')
    f_tidy_tagdb = open(file_path, 'w') 

    for line in f_tagdb:
        movie = json.loads(line)

        media_type = movie['mediaType']

        language = movie['spokenLanguages']
        language = __handle_language_for_tagdb(language)

        genres = movie['genres']
        genres = __handle_genres_for_tagdb(genres)
        if len(genres) == 0:
            continue 

        runtime = movie['runtime']

        mawid = []

        ids = movie['externalIds']

        movie_dic = dict()
        movie_dic['mediaType'] = media_type
        movie_dic['ids'] = ids
        movie_dic['language'] = language
        movie_dic['genres'] = genres
        movie_dic['mawid'] = mawid
        movie_dic['runtime'] = runtime

        movie_json = json.dumps(movie_dic)
        f_tidy_tagdb.write(movie_json + '\n')

    f_tidy_tagdb.close()
    f_tagdb.close()



def generate_imdb_json_from_tidy_tagdb_tmp(file_path):
    f_tidy_ids = open(file_path)
    f_imdb_json_from_tidy_ids = open('imdb_json_from_tidy_ids.json', 'w')

    new_movie_dic = dict()
    for line in f_tidy_ids:
        movie = json.loads(line)
        ids = movie['ids']

        try:
            imdbId = ids['imdbId']
            new_movie_dic[imdbId] = movie
        except KeyError:
            continue
    
    movie_json = json.dumps(new_movie_dic)
    f_imdb_json_from_tidy_ids.write(movie_json + '\n')



def get_tidy_tagdb(file_path):
    f_tidy_tagdb_tmp = open(file_path)
    f_tidy_tagdb = open('tidy_tagdb.json', 'w') 
    f_imdb_json_from_tidy_ids = open('imdb_json_from_tidy_ids.json')

    imdb_json_movie = json.loads(f_imdb_json_from_tidy_ids.readline())

    count = 0
    for line_of_f_tidy_tagdb_tmp in f_tidy_tagdb_tmp:
        movie = json.loads(line_of_f_tidy_tagdb_tmp)
        ids = movie['ids']

        try:
            imdbId = ids['imdbId'] 
            info = imdb_json_movie[imdbId]['info']           
            mawid = info['mawid']
            
            movie['mawid'] = mawid

            movie_json = json.dumps(movie)

            f_tidy_tagdb.write(movie_json + '\n')
            print 1

        except KeyError:
            pass

    f_tidy_tagdb.close()
        
  
        


#######################################################################


#get_tidy_ids('tidy_ids.json')

#delete_unusefull_info('tidy_tagdb_tmp.json')

#generate_imdb_json_from_tidy_tagdb_tmp('tidy_ids.json')

get_tidy_tagdb('tidy_tagdb_tmp.json')




#check_empty_of_ids('tidy_ids.json', 'free')

































