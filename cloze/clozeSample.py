
#from crf_functions import *
import requests
import json
import pprint

search_query = 'the $ would be redeemed in five years , subject to terms of the company’s debt.'


a = [{ "src" : search_query }]
headers = {'Content-type': 'application/json'}
r = requests.post('http://nlp-ultron.cs.nthu.edu.tw:7276/translator/translate', data = json.dumps(a) , headers=headers).json()

possible_held_out_word = [i['tgt'] for i in r[0]]
pprint.pprint(possible_held_out_word)