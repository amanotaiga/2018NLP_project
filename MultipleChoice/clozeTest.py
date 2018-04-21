# coding: utf-8
#from crf_functions import *
import requests
import json
import pprint
import re
text = []
textS = []
searchList = []
searchList.append('convert')
searchList.append('software')

def load_data():
    for line in open('essay.txt', 'r',encoding='utf-8'):
        if line.strip() != '':
            text.append([line.strip().split('\t')])
            textS.append(words(line))
            #print(text)
    return textS

def words(text): return re.findall(r'\w+', text.lower())
sentenceList = []

def showSentence(text):
    sentence = []
    for search in searchList:
        for i in range(len(text)):
            if search in text[i]:
                ind = text[i].index(search)
                text[i][ind] = '___'
                sentence = ' '.join(text[i])
                sentenceList.append(sentence)
                break
    return sentenceList

def giveSentence():
    t = words(open('essay.txt').read())
    text = load_data()
    return showSentence(text)

def giveSearchVol():
    return searchList
# for sentence in sentenceL:
#     print(sentence)




