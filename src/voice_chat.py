import speech_recognition as sr
import pyttsx3

# Inisialisasi engine suara
engine = pyttsx3.init()
engine.setProperty("rate", 170)  # kecepatan bicara
engine.setProperty("volume", 1.0)

# Fungsi untuk berbicara
def speak(text):
    print("🤖:", text)
    engine.say(text)
    engine.runAndWait()

# Inisialisasi recognizer
r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("\n🎙️ Ucapkan sesuatu ('keluar' untuk berhenti)...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        
        text = r.recognize_google(audio, language="id-ID").lower()
        print("🗣️ Kamu bilang:", text)

        if "keluar" in text:
            speak("Oke, sampai jumpa lagi!")
            break

        # Di sini kamu bisa ganti dengan logika chatbot-mu nanti
        response = f"Kamu berkata '{text}'. Aku mendengarnya dengan jelas."
        speak(response)

    except sr.UnknownValueError:
        print("❌ Aku tidak mendengar dengan jelas. Coba ulangi.")
    except sr.RequestError as e:
        print(f"🌐 Error pada Google API: {e}")
    except KeyboardInterrupt:
        print("\n👋 Dihentikan secara manual.")
        break
