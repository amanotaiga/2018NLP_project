
#from crf_functions import *
import requests
import json
import pprint

#search_query = 'The companies are fighting back and $ authorities to crack down on the boxes.'

def searchChoice(search_query):
    a = [{ "src" : search_query }]
    headers = {'Content-type': 'application/json'}
    r = requests.post('http://nlp-ryze.cs.nthu.edu.tw:7276/translator/translate', data = json.dumps(a) , headers=headers).json()
    possible_held_out_word = [i['tgt'] for i in r[0]]
    #pprint.pprint(possible_held_out_word)
    return possible_held_out_word