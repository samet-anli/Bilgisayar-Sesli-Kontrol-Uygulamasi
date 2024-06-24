import datetime
from logging import root
import time
import webbrowser
from gtts import gTTS  # Doğru şekilde tanımlanmış olan gTTS sınıfını içe aktarın
from playsound import playsound
#pyaudio yu gTTs kullanıyor. Google
#yazıyı ses çevirme eklentisi.
import speech_recognition as sr
import os
import subprocess

r = sr.Recognizer()
def record(ask = False):   
    with sr.Microphone() as source: 
    #sesi hangi kaynaktan alıcağını belirledik.
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan: Anlayalamadım")
            speak("Anlamadım")
        except sr.RequestError:
            print("Asistan: Sistem Çalışmıyor. \ninterneti kontrol edin.")
        return voice

def speak(string):
    tts = gTTS(text=string, lang = "tr", slow=False)
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)
    
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
lumion_path = r'D:\Lumion 12.5 Student\Lumion.exe'                      # isim
autoCad_path = r'C:\Program Files\Autodesk\AutoCAD 2024\acad.exe'
sketchub_path = r'C:\Program Files\SketchUp\SketchUp 2023\SketchUp.exe' # isim
d3max_path = r'C:\Program Files\Autodesk\3ds Max 2024\3dsmax.exe'
revit_path = r'C:\Program Files\Autodesk\Revit 2023\Revit.exe'
shop_path = r'C:\Program Files\Adobe\Adobe Photoshop 2021\Photoshop.exe'
google_earth_path = r'C:\Program Files\Google\Google Earth Pro\client\googleearth.exe'
pes17_path = r'C:\Program Files (x86)\Pro Evolution Soccer 2017\PES2017.exe'

def response(voice):
    if voice != '':
        voice = voice.lower()
        print(voice)
    if "merhaba" in voice:
        speak("Boş Yapma")
    if "chrome aç" in voice:
        speak("açıldı")
        subprocess.run([chrome_path])
    if "krom kapa" in voice:
        speak("kapatıldı")
        subprocess.run(["taskkill", "/f", "/im", "chrome.exe"])
    if "hangi gündeyiz" in voice:
        today = time.strftime("%A")
        speak(today)
    if "görüşürüz" in voice:
        speak("görüşürüz aşkım")
    if "saat kaç" in voice:
        saat = datetime.datetime.now().strftime("%H:%M")
        speak(saat)
    if "google'da ara" in voice:
        speak("Ne arayayım")
        search = record()
        url = "https://www.google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        webbrowser.Chrome.open_new_tab()
        speak("Al bak.")
        #*-******************
    if "3d max aç" in voice:
        speak("tamam Emirhan bey açıyorum.")
        subprocess.run([d3max_path])
    if "autocad aç" in voice:
        speak("Açtım Aşkım")
        subprocess.run([autoCad_path])
    if "revit aç" in voice:
        speak("Revit sana yasak ama neyse")
        subprocess.run([revit_path])
    if "photoshop aç" in voice:
        speak("hı Açtım")
        subprocess.run([shop_path])
    if "google earth aç" in voice:
        speak("Açtımm")
        subprocess.run([shop_path])
    if "pes aç" in voice:
        speak("Bensiz mi?")
        subprocess.run([pes17_path])
    if "su aç" in voice:
        speak("bir içim")
        subprocess.run([lumion_path])
    if "ekmek aç" in voice:
        speak("ekmek parası")
        subprocess.run([sketchub_path])
        
def start_nasibe():
    voice = record()
    response(voice)


