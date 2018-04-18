import re
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize,pos_tag

def words(text): return re.findall(r'\w+', text.lower())

text = []
text2 = []

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
    for line in open('essay.txt', 'r',encoding='utf-8'):
        token = words(line)
        for vol in token:
            text2.append(vol)
        text.append(token)
    return text2

text = loadVerbData()
#print(text)

def pos():
    for searchWord in text2:
         k = pos_tag([searchWord])[0][1]
         #print(pos_tag([searchWord])[0])
         m = get_wordnet_pos(k)
    return m


