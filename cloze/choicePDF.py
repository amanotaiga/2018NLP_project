from reportlab.pdfgen import canvas
import textwrap
import ast
import codecs
import clozeTest
import Verbroot
fname = 'detail.txt'

def long_length(string,offset,key):
    wrap_text = textwrap.wrap(string, width=75)
    c.drawString(100, 750 - offset,str(key + 1) + ":  ")
    for text in wrap_text:
        c.drawString(115, 750 - offset, text)
        offset = offset + 10
    return offset

def loadFile():
    #read dictionary file
    with open(fname,'r') as f:
        dict_from_file =  ast.literal_eval(f.read())

# create pdf
c = canvas.Canvas("test.pdf")
offset = 0
c.setFont('Helvetica-Bold', 25)
c.drawString(100, 800,' choice test')

sentence = []
choiceList  = []

def drawChoice(choiceList,offset):
    c.setFont('Helvetica-Bold', 10)
    c.drawString(130, 750 - offset - 10, choiceList[0])
    c.drawString(130, 750 - offset - 20, choiceList[1])
    c.drawString(200, 750 - offset - 10, choiceList[2])
    c.drawString(200, 750 - offset - 20, choiceList[3])
    print(choiceList)
    return

sentence = []
# sentence.append("one of the biggest problems is the ___ availability of the streaming boxes")
# sentence.append("The companies are fighting back and pushing authorities to crack down on the boxes")
sentence = clozeTest.giveSentence()

choiceList = []
# choiceList = [["huge","awesome","right","nice"],["happy","sad","furious","interesting"]]
choiceList = Verbroot.giveNearVol()

offset= 0

for key in range(len(sentence)):
    c.setFont('Helvetica-Bold', 10)
    if offset>=700:
        c.showPage()
        offset = 0
        offset = offset+10
    if len(sentence[key]) > 75:
        offset = long_length(sentence[key],offset,key)
    else:
        c.drawString(100, 750 - offset, str(key+1)+":  "+sentence[key])
        print(sentence[key])
    drawChoice(choiceList[key],offset)
    offset = offset+40

c.save()
