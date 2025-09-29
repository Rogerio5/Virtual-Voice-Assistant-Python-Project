# CPATURA DE VOZ COM MICROFONE 
import speech_recognition as sr

def ouvir_microfone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Pode falar...")
        audio = r.listen(source)
    try:
        texto = r.recognize_google(audio, language='pt-BR')
        print("Você disse:", texto)
        return texto
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
        return ""
    except sr.RequestError:
        print("Erro ao conectar com o serviço de reconhecimento.")
        return ""

# RESPOSTA COM VOZ 
from gtts import gTTS
import os

def speak(texto):
    tts = gTTS(text=texto, lang='pt-br')
    tts.save("resposta.mp3")
    os.system("start resposta.mp3")  # No Mac/Linux use 'afplay' ou 'mpg123'

# INTERPRETAÇÃO DE COMANDOS 
import webbrowser
import random

def interpretar_comando(texto):
    texto = texto.lower()
    if "youtube" in texto:
        query = texto.replace("youtube", "").strip()
        url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(url)
        respostas = [
            "Abrindo o YouTube pra você.",
            "YouTube na área, chefe!",
            "Missão YouTube iniciada."
        ]
        return random.choice(respostas) + f" Procurando por '{query}'."
    elif "wikipedia" in texto:
        query = texto.replace("wikipedia", "").strip()
        url = f"https://pt.wikipedia.org/wiki/Especial:Pesquisar?search={query}"
        webbrowser.open(url)
        return f"Abrindo Wikipedia sobre '{query}'."
    elif "farmácia" in texto:
        url = "https://www.google.com/maps/search/farmácia+perto+de+mim"
        webbrowser.open(url)
        return "Mostrando farmácias próximas no Google Maps."
    else:
        return "Desculpe, não entendi o comando."

# FLUXO COMPLETO 
texto = ouvir_microfone()
if texto:
    resposta = interpretar_comando(texto)
    speak(resposta)
else:
    speak("Não consegui entender o que você disse.")

