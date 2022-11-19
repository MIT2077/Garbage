import pyaudio
import SpeechRecognition as sr
import time
import os
import sys

#Create voice assistant using SpeechRecognition

#Create a function to record audio and return it as a string
def recordAudio():
    #Record the audio
    r = sr.Recognizer() #Create a recognizer
    #Open the microphone and start recording
    with sr.Microphone() as source:
        print('Say something!')
        audio = r.listen(source)

    #Use Google's speech recognition
    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: ' + data)
    except sr.UnknownValueError:
        print('Google Speech Recognition could not understand audio')
    except sr.RequestError as e:
        print('Request results from Google Speech Recognition service error' + e)

    return data

#Create a function to get the virtual assistant response
def assistantResponse(text):
    print(text)

    #Convert the text to speech
    os.system('say ' + text)

#Create a function for wake words or phrase
def wakeWord(text):
    WAKE_WORDS = ['hey computer', 'okay computer'] #A list of wake words

    text = text.lower() #Convert the text to all lower case words

    #Check to see if the users command/text contains a wake word/phrase
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    #If the wake word isn't found in the text from the loop
    return False

#Create a function to get the date
def getDate():

        now = datetime.datetime.now()
        my_date = datetime.datetime.today()
        weekday = calendar.day_name[my_date.weekday()] #e.g. Monday
        monthNum = now.month
        dayNum = now.day

        #A list of months
        month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

        #A list of ordinal numbers
        ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']

        return 'Today is ' + weekday + ' ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1] + '.'

#Create a function to return a random greeting response
def greeting(text):
    #Greeting inputs
    GREETING_INPUTS = ['hi', 'hey', 'hola', 'greetings', 'wassup', 'hello']

    #Greeting responses
    GREETING_RESPONSES = ['howdy', 'whats good', 'hello', 'hey there']

    #If the users input is a greeting, then return a randomly chosen greeting response
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'

    #If no greeting was detected then return an empty string
    return ''

#Create a function to get a person's first and last name from the text
def getPerson(text):

        wordList = text.split() #Split the text into a list of words

        for i in range(0, len(wordList)):
            if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i + 1].lower() == 'is':
                return wordList[i + 2] + ' ' + wordList[i + 3]


#1: Wake up
time.sleep(1)
assistantResponse('What can I do for you?')
while True:
    #2: Record the audio
    text = recordAudio()
    response = '' #Create a response variable

    #3: Check for the wake word/phrase
    if (wakeWord(text) == True):

        #4: Check for greetings by the user
        response = response + greeting(text)

        #5: Check to see if the user said date
        if ('date' in text):
            get_date = getDate()
            response = response + ' ' + get_date

        #6: Check to see if the user said time
        if ('time' in text):
            now = datetime.datetime.now()
            meridiem = ''
            if now.hour >= 12:
                meridiem = 'p.m' #Post meridiem (PM), after midday
                hour = now.hour - 12
            else:
                meridiem = 'a.m' #Ante meridiem (AM), before midday
                hour = now.hour

            #Convert minute into a proper string
            if now.minute < 10:
                minute = '0' + str(now.minute)
            else:
                minute = str(now.minute)

            response = response + ' ' + 'It is ' + str(hour) + ':' + minute + ' ' + meridiem + '.'

        #7: Check to see if the user said 'who is'
        if ('who is' in text):
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences=2)
            response = response + ' ' + wiki

        #8: Have the assistant respond back using audio and text from response
        assistantResponse(response)

#Run the program






