import re
from collections import defaultdict, Counter,OrderedDict
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize,pos_tag
from nltk.corpus import wordnet
import random
import clozeTest
# import other python files
#  import readvolDic

# position
#nltk.download("wordnet")
#nltk.download("averaged_perceptron_tagger")
#nltk.download("punkt")

#lemmatizer = WordNetLemmatizer()

text = dict()
volFreq = OrderedDict()

def words(text): return re.findall(r'\w+', text.lower())

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

def lemmatize_sentence(sentence):
    res = []
    lemmatizer = WordNetLemmatizer()
    for word, pos in pos_tag(word_tokenize(sentence)):
        wordnet_pos = get_wordnet_pos(pos) or wordnet.NOUN
        res.append(lemmatizer.lemmatize(word, pos=wordnet_pos))

    return res,wordnet_pos

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

"""
def searchV(searchVerb):
    for vRoot, vVar in txtVerb.items():
        for vVar in txtVerb[vRoot]:
            if vVar == searchVerb:
                print(vRoot)
    return vRoot
"""
def searchV(searchVerb):
    for vRoot, vVar in txtVerb.items():
        if searchVerb in txtVerb[vRoot]:
            vR = vRoot
        else:
            vR = lemmatize_sentence(searchVerb)
    return vR

#txtVerb = loadVerbData()
#print(searchV("working"))

def findNearbyVol(searchVol):
    volNear = []
    volNear.append(searchVol)
    if(volFreq[searchVol]):
        volIndex = list(volFreq.keys()).index(searchVol)
        R = random.sample(range(-100, 100), 190)
        index = 0
        while(len(volNear) < 4):
            volNearby = list(volFreq)[volIndex + R[index]]
            if (volFreq[volNearby][0] == get_wordnet_pos(pos_tag([searchVol])[0][1])):
                if(not [item for item, count in Counter(volNear).items() if count > 1]):
                    volNear.append(volNearby)
            index = index + 1
    return volNear

def giveNearVol():
    searchWordList = clozeTest.giveSearchVol()
    volFreq = loadfreqData()
    nearVolL = []
    for searchWord in searchWordList:
        vol = findNearbyVol(searchWord)
        print(searchWord)
        nearVolL.append(vol)
    return nearVolL

#print(giveNearVol())


#searchWord = 'nice'
#searchWordList = clozeTest.giveSearchVol()

#print(pos_tag([searchWord]))
#print(get_wordnet_pos(pos_tag([searchWord]))

"""
# give root of word
print(lemmatize_sentence(word))
"""

#print(volFreq['whole'])


#check dupicate element
#print([item for item, count in Counter(z).items() if count > 1])
