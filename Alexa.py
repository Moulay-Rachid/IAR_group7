import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import smtplib
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_commend():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "")
                print(command)
    except:
        pass
    return command

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('alexarobot92@gmail.com', 'alexa92robot')
    email = EmailMessage()
    email['From'] = 'alexarobot92@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

email_list = {
    'pink': 'programmeurdz92@gmail.com',
    'black': 'moulayrach2016@gmail.com',
    'whit': 'hai19med94@gmail.com'
}

def run_alexa():
    command = take_commend()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("current time is" + time)
    elif "who is" in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif "date" in command:
        talk("sorry, I have a headache")
    elif "joke" in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(pyjokes.get_joke())
    elif "send message" in command:
        talk("to whom you want to send email")
        name = take_commend()
        receiver = email_list[name]
        print(receiver)
        talk("what is the subject of your email")
        subject = take_commend()
        talk("tell me the text in your email")
        message = take_commend()
        send_email(receiver, subject, message)
    elif "open the door" in command:
         print("the door opening")
         talk("the door opening")

    else:
        talk("please say the command again.")

while True:
    run_alexa()
