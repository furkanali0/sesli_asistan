import pyaudio
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time




kayıt = sr.Recognizer()
def dinleme(a =False):
    with sr.Microphone() as kaynak:
        if a:
            print(a)
        mikrofon = kayıt.listen(kaynak)
        ses = ""
        try :
            ses = kayıt.recognize_google(mikrofon, language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan : Anlayamadım.")
        except sr.RequestError:
            print("Asistan : Sistem Şu Anda Çalışmıyor")

        return ses
def konusma(metin):
    tts = gTTS(text=metin, lang="tr", slow=False)
    ses = "konusma.mp3"
    tts.save(ses)
    playsound("konusma.mp3")
    os.remove(ses)

def yanıt(ses):
    if "merhaba" in ses:
        konusma("Sanada merhaba dostum")
    if "çıkış" in ses:
        konusma("Çıkış yapılıyor")
        quit()
    if "youtube" in ses:
        konusma("Youtube Açılıyor")
        youtube()
        
         
def youtube():
    path = "C:\\Users\Furkan Ali\Desktop\chromedriver\chromedriver.exe"
    browser = webdriver.Chrome(executable_path=path)
    konusma("Ne açmamı istersin")
    browser.get('https://youtube.com')
    time.sleep(6)
    
    while True: 
        
        a = dinleme(ses)
        time.sleep(2)
        browser.find_element(By.XPATH, '//input[@id="search"]').send_keys(a)
        browser.find_element(By.XPATH, "//button[@id='search-icon-legacy']").click()
        time.sleep(4)
        browser.find_element(By.XPATH, '//input[@id="search"]').clear()
        if "Kapat" in a:
            browser.close()
            break
            
        
    
    
    
konusma("Hoşgeldin")
print("Başlatıldı...")
while True:
    ses = dinleme()
    if bool(ses)== True:
        print(ses)
        ses = ses.lower()
        yanıt(ses)