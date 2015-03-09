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

def __combine_ids(ids, f_tidy_ids):
    print ids
    freebaseId_list = []
    imdbId_list = []
    wikipediaPageId_list = []
    tmdbId_list = []

    # for k in ids:
    #     if k == 'freebaseId':
    #         for line in f_tidy_ids:
    #             if line['ids']




def get_tidy_tagdb(file_path):
    f_tagdb = open('!tagdb.json')
    f_tidy_tagdb = open('tidy_tagdb.json', 'w') 

    count = 0
    for line_of_f_tagdb in f_tagdb:
        movie = json.loads(line_of_f_tagdb)

        media_type = movie['mediaType']

        language = movie['spokenLanguages']
        language = __handle_language_for_tagdb(language)
        #print language

        genres = movie['genres']
        genres = __handle_genres_for_tagdb(genres)

        runtime = movie['runtime']

        mawid = []

        ids = movie['externalIds']
        for i in ids:
            #count += 1
            f_tidy_ids = open('tidy_ids.json')            
            for line_of_f_tidy_ids in f_tidy_ids:
    
                movie_of_ids = json.loads(line_of_f_tidy_ids) 
                ids_in_tidy_ids = movie_of_ids['ids']
                info_in_tidy_ids = movie_of_ids['info']                

                for j in ids_in_tidy_ids:
                    #print i, j
                    count += 1
                    if i == j and ids[i] == ids_in_tidy_ids[j]:   
                        print 0                      
                        mawid = info_in_tidy_ids['mawid']
                #print i
            f_tidy_ids.close()
            #print i  

        movie_dic = dict()
        movie_dic['mediaType'] = media_type
        movie_dic['ids'] = ids
        movie_dic['language'] = language
        movie_dic['genres'] = genres
        movie_dic['mawid'] = mawid
        
        movie_json = json.dumps(movie_dic)
        f_tidy_tagdb.write(movie_json + '\n')

    f_tidy_tagdb.close()

    print count    
        


#######################################################################


#get_tidy_ids('tidy_ids.json')
get_tidy_tagdb('tidy_tagdb.json')


#check_empty_of_ids('tidy_ids.json', 'free')

































