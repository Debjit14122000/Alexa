import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener =sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice =listener.listen(source)
            command =listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','') # It returns a new substring with replacement.
                #print(command) #print command without the alexa word

    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in  command:
        song=command.replace('play','')
        talk('playing....'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%S %p')
        print(time)
        talk('Current time is:-'+time)
    elif 'who is the  ' in command:
        person=command.replace('who is the  ','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)

    elif 'date' in command:
        print("please see it in your clock")
        talk("please see it in your clock")
    elif 'are you single' in command:
        print("Yes! I am in a relationship with wifi")
        talk("Yes! I am in a relationship with wifi")
    elif 'i love you' in command:
        print("Thank you! I also Love you.But I have a boyfriend")
        talk("Thank you! I also Love you.But I have a boyfriend")
    elif 'give me your introduction' in command:
        print("I am DEBJIT GHOSH .My father name is BISWAJIT GHOSH and my mother name is PALLABI GHOSH.I live in ASANSOL BURNPUR and my pin code is 713325.my mobile number is 7001805791")
        talk("I am DEBJIT GHOSH .My father name is BISWAJIT GHOSH and my mother name is PALLABI GHOSH.I live in ASANSOL BURNPUR and my pin code is 713325.my mobile number is 7001805791")
    elif 'what is mrityunjaya mantra' in command:
        print("ooooooom traimbakam yajamaha sugandhi pustibardhanam urbarukamabi bandhanam mrityurmukshi maaamritam ooooooom ")
        talk("ooooooom traimbakam yajamaha sugandhi pustibardhanam urbarukamabi bandhanam mrityurmukshi maaamritam ooooooom")
    elif 'what is father name of my baba' in command:
        print("LATE HARI NARAYAN GHOSH")
        talk("LATE HARI NARAYAN GHOSH")
    elif 'good night' in command:
        print("OKAY!! tata bye good night....see you again later")
        talk("OKAY!! tata bye good night....see you again later")
run_alexa()