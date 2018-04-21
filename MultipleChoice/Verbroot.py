import re
from collections import defaultdict, Counter,OrderedDict
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize,pos_tag
from nltk.corpus import wordnet
import ast
from pprint import pprint
import random
import string
import clozeTest
import clozeSample
import timeit

# import other python files
#  import readvolDic

# position
#nltk.download("wordnet")
#nltk.download("averaged_perceptron_tagger")
#nltk.download("punkt")

text = dict()
volFreq = OrderedDict()

#def words(text): return re.findall(r'\w+', text)
def words(text): return re.findall(r'\w+|[.,!?;]+', text)

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return 'j'
    elif treebank_tag.startswith('V'):
        return 'v'
    elif treebank_tag.startswith('N'):
         return 'n'
    elif treebank_tag.startswith('R'):
        return 'r'
    elif treebank_tag.startswith('D') or treebank_tag.startswith('PDT'):
        return 'dt'
    elif treebank_tag.startswith('PR'):
        return 'pron'
    elif treebank_tag.startswith('CC'):
        return 'c'
    elif treebank_tag.startswith('IN') or treebank_tag.startswith('TO'):
        return 'prep_conj'
    else:
        return 'None'

def loadVerbData():
    for line in open('gec.pattern.verb.txt', 'r'):
        token = words(line)
        text[token[0]] = token[1:]
    return text

def loadfreqData():
    for line in open('vol_freq.txt', 'r'):
        num,word,pos,freq,disper =  line.strip().split('\t')
        word = word.strip()
        volFreq[word] = pos,freq
    return volFreq

def searchV(searchVerb):
    for vRoot, vVar in txtVerb.items():
        if searchVerb in txtVerb[vRoot]:
            vR = vRoot
        else:
            vR = lemmatize_sentence(searchVerb)
    return vR

#txtVerb = loadVerbData()
#print(searchV("working"))

def imperative_pos_tag(sent):
    return pos_tag(['He']+sent)[1:]

vocList = []
#read VocList file
def readVocList(fname):
    with open(fname,'r') as f:
        dict_from_file =  ast.literal_eval(f.read())
    return dict_from_file

# extract useful information from evp VocList
def extractVocList(vocL,needList):
    tmp = defaultdict(lambda:dict())
    for key in vocL:
        for item in needList:
            tmp[key][item] = vocL[key][item]
    return tmp

def findExample(wordL):
    searchQuery = list()
    search = defaultdict(lambda :0)
    for word in wordL:
        searchQuery.append((words(excVocList[word]['lear_examp'])))
        if word in searchQuery[-1]:
            ind = searchQuery[-1].index(word)
            searchQuery[-1][ind] = '$'
            search[word] = ' '.join(searchQuery[-1])
    #print(search)
    return search

def filterChoice(sentenceL):
    tmpChoice = list()
    tmpL = list()
    Choice = defaultdict(lambda :list())
    for word in sentenceL:
        tmpL[:] = []
        tmpL.append(word)
        Choice[word].append(word)
        tmpChoice.append(clozeSample.searchChoice(sentenceL[word]))
        x = [''.join(c for c in s if c not in string.punctuation) for s in tmpChoice[-1]]
        x = [s for s in x if s!='unk' and len(s)>1]
        tmpChoice[-1] = x
        posWord = (pos_tag([word]))
        for possibleChoice in tmpChoice[-1]:
            posChoice = (pos_tag([possibleChoice]))
            if (posWord[0][1] == posChoice[0][1] and len(tmpL)<4 and possibleChoice not in tmpL):
                tmpL.append(possibleChoice)
                Choice[word].append(possibleChoice)
                # if([item for item, count in Counter(tmpL).items() if count > 1]):
                #     del tmpL[-1]
    return Choice

def giveMultipleQuestion():
    tmpSentence = list()
    tmpChoice = list()
    tmpKey = list()
    tmp = list()
    for key,word in zip(sentenceDict,ChoiceDict):
        tmpKey.append(key)
        ind = sentenceDict[key].index('$')
        tmp = sentenceDict[key][:ind] + '___' + sentenceDict[key][ind + 1:]
        tmpSentence.append(tmp)
        tmpChoice.append(ChoiceDict[key])
    return tmpKey,tmpSentence,tmpChoice

vocList = readVocList('detail.txt')
#displayDict(vocList)
#print(vocList)
# store items want to be extracted
itemList = ['level','lear_examp']
excVocList = extractVocList(vocList,itemList)
#pprint(excVocList)

wordList = []
wordList = ['airport','strong','work']
sentenceDict = findExample(wordList)
ChoiceDict = filterChoice(sentenceDict)


