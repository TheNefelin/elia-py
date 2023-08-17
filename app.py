from gtts import gTTS #texto a voz
import speech_recognition as sr #voz a texto
import os # reproductor

r = sr.Recognizer()
txt = ""

with sr.Microphone() as source:
    print("Dí Algo...")
    audio = r.listen(source)

    try:
        txt = r.recognize_google(audio, language="es-us")
        print(txt)
    except:
        print("ERROR")

with open('leer.txt', 'w') as f:
    f.write(txt)

speech = gTTS(text = str(txt), lang = "es-us", slow = False)
speech.save("resp.mp3")
os.system("start resp.mp3")
