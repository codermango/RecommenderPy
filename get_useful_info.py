#!coding=utf-8
import json



######################################################################
# help function

def handle_country_link(country):
    country_list = []

    for item in country:
        if item.startswith('http'):
            

    return country_list




#######################################################################



f_ids_info = open('!ids_info.json')
f_imdbinfo = open('!imdbinfojson.json')
f_tagdb = open('!tagdb.json')


f_tidy_ids = open('tidy_ids.json', 'w')

for line in f_ids_info:
    movie = json.loads(line)
    info = movie['info']
    language = info['language']
    country = info['country']


    mawid1 = info['mawid1']
    mawid2 = info['mawid2']
    mawid = list(set(mawid1).union(set(mawid2)))

    #print type(mawid1)

    info_dic = dict()
    info_dic['mawid'] = mawid
    info_dic['language'] = language
    info_dic['country'] = country

    #print info_dic

    movie_dic = dict()
    movie_dic["info"] = info_dic
    movie_dic['ids'] = movie['ids']

    #print movie_dic

    movie_json = json.dumps(movie_dic)
    f_tidy_ids.write(movie_json+'\n')
    #f_tidy_ids.write('mark')
    #print movie_json

    


f_tidy_ids.close()


	
	






