import pyttsx3
import os
from gtts import gTTS #Import Google Text to Speech
# initialisation 
engine = pyttsx3.init() 

passw='12345'
authenticate=''
name='david'
flag=0
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say('Welcome')
engine.runAndWait()
while True:
    if (authenticate!=passw and flag==0):
        engine.say('Authenticate your self')
        engine.runAndWait()
        au=input()
        if ('stop' in au or 'exit' in au or 'terminate' in au):
            engine.say('ok sir as you wish ,thank you')
            engine.say('I am shutting down')
            engine.runAndWait()
            break
        elif (au==passw):
            flag=1
            engine.say('you are welcome')
            engine.runAndWait()
        else:
            engine.say('Sorry ,we could not recognize you')
            engine.runAndWait()
    if (flag==1):
        engine.say("I am here to help you ,please say your requirement")
        engine.runAndWait()
        p=input()
        
        if(('your' in p and 'name' in p and 'change' not in p)or('who' in p or 'you' in p )or('what' in p or ('your' in p and 'identity' in p ) )):
            engine.say('My name is ')
            engine.say(name)
            engine.runAndWait()
        elif ('your' in p and 'name' in p and 'change'):
            engine.say('ok sir ,what name you suggest')
            engine.runAndWait()
            p=input()
            name=p
            engine.say('my name is update to')
            engine.say(name)
            engine.say('Thank you for new name')
            engine.runAndWait()
        elif (name in p or 'online' in p or ('you'in p and ('there' in p or 'online' in p))):
            engine.say('ya sir , i am online ')
            engine.runAndWait()
        elif ('stop' in p or 'exit' in p or 'terminate' in p or 'shut down' in p ):
            engine.say('ok sir as you wish ,thank you')
            engine.say('I am shutting down')
            engine.runAndWait()
            break
        elif (name in p) and ('change' not in p):
            engine.say('yes sir')
            engine.runAndWait()
        elif (name in p) and ('change' not in p):
            engine.say('yes sir')
            engine.runAndWait()
        elif (("run" in p) or ('open' in p) or  ("execute" in p )) and  (("notepad" in p) or ("editor" in p) ) :
            os.system("notepad")
            engine.say('notepad is opened sir')
            engine.runAndWait()
        elif (("run" in p) or  ("execute" in p ) or ('open' in p)) and  (("intellij" in p) or ("java" in p) ) :
            engine.say('Ok sir, i am opening intellij idea for java programming')
            engine.say('thank you')
            engine.runAndWait()
            os.system("idea64")
        else:
            engine.say('i can not understand what you are saying')
            engine.say('Sorry sir,I am not programmed to fullfill this request')
            engine.runAndWait()
