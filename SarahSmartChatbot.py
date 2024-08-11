import openai
import pyttsx3
import speech_recognition as sr
import webbrowser


openai.api_key = "ADD OPENAI API KEY" 

# It is not allowed to add API to GITHUB, so please contact me from my resume to get the API key. Thanks. :)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_openai_response(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Sarah, a helpful assistant."},
            {"role": "user", "content": question}
        ],
        max_tokens=150
    )
    return response.choices[0].message['content'].strip()

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(f"User: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None

if __name__ == '__main__':
    speak("Hello, I'm Sarah. How may I assist you today?")
    
    while True:
        command = listen_command()
        if command:
            if 'quit chat' in command or 'bye' in command:
                speak("Goodbye! Have a great day!")
                break
            
            response = get_openai_response(command)
            print(f"Sarah: {response}")
            speak(response)
            
            if 'open youtube' in command:
                webbrowser.open("https://www.youtube.com")
            if 'open google' in command:
                webbrowser.open("https://www.google.com")
