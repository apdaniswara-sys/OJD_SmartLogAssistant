# src/voice_utils.py
import speech_recognition as sr
import threading

# Natural TTS with fallback
try:
    from TTS.api import TTS
    # Gunakan model Bahasa Indonesia (offline model)
    # Model ini otomatis diunduh pertama kali (1x saja)
    tts_engine = TTS(model_name="tts_models/id/indonesian/female-glow-tts", progress_bar=False, gpu=False)
    use_coqui = True
except Exception as e:
    print("⚠️ Coqui-TTS tidak ditemukan atau gagal load, fallback ke pyttsx3:", e)
    import pyttsx3
    tts_engine = pyttsx3.init()
    tts_engine.setProperty('rate', 170)
    use_coqui = False


def listen():
    """Dengarkan suara user dan konversi ke teks."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Silakan bicara...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="id-ID")
            print(f"🗣️ Kamu bilang: {text}")
            return text
        except sr.UnknownValueError:
            return "Maaf, saya tidak mendengar dengan jelas."
        except sr.RequestError:
            return "Error: layanan pengenalan suara tidak tersedia."


def speak(text):
    """Ucapkan teks dengan suara natural (Coqui jika tersedia)."""
    def _speak():
        try:
            if use_coqui:
                # Gunakan suara Indonesia
                tts_engine.tts_to_file(text=text, file_path="temp_output.wav")
                import simpleaudio as sa
                wave_obj = sa.WaveObject.from_wave_file("temp_output.wav")
                play_obj = wave_obj.play()
                play_obj.wait_done()
            else:
                tts_engine.say(text)
                tts_engine.runAndWait()
        except Exception as e:
            print("❌ Error saat berbicara:", e)

    threading.Thread(target=_speak, daemon=True).start()
