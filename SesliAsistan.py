import speech_recognition as sr
import json
import os
import subprocess
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Dinliyorum aga söyle:")
    r.adjust_for_ambient_noise(source, duration=0.2)
    audio = r.listen(source)
    text = r.recognize_google(audio)
    text = text.lower()

if text.lower() == "turn off my pc":
    os.system("shutdown /s /t 120")
    print("Bilgisayarı kapatıyorum")
if text.lower() == "turn on spotify":
    subprocess.call(["C:\\Users\\dyunu\\AppData\\Local\\Discord\\app-1.0.9010\\Discord.exe"])

with open("yazı.txt","w",encoding="utf-8") as f:
    f.write(text)