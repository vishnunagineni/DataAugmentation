import googletrans
import json 
from googletrans import Translator
translator=Translator()
backtranslator=Translator()
with open('Intent.json','r') as file:
    data=json.load(file)

realdata=[]
for intent in data['intents']:
    if intent['intent']=='CourtesyGreetingResponse':
        realdata=intent['responses']
        break
generateddata=[]
for i in realdata:
    ttext=translator.translate(i,src='en',dest='fr')
    print(ttext.text)
    btext=backtranslator.translate(ttext.text)
    print(btext.text)
    generateddata.append(btext.text)

print(generateddata)

#btext=backtranslator.translate(ttext.text,src='fr',dest='en')
#print(btext.text)
