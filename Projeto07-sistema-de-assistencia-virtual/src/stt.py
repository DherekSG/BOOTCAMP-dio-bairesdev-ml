import speech_recognition as sr

def transcribe_ptbr(timeout=5, phrase_time_limit=8):
    """Escuta do microfone e retorna texto em pt-BR usando a API gratuita do Google."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        r.energy_threshold = 300  # pode ajustar dinamicamente com: r.adjust_for_ambient_noise(source, duration=1)
        print("🎙️  Fale seu comando...")
        audio = r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
    try:
        text = r.recognize_google(audio, language="pt-BR")
        print(f"📝 Você disse: {text}")
        return text.lower().strip()
    except sr.WaitTimeoutError:
        print("⏳ Tempo esgotado sem fala detectada.")
        return ""
    except sr.UnknownValueError:
        print("🤷 Não entendi o que você disse.")
        return ""
    except sr.RequestError as e:
        print(f"🌐 Erro no serviço de STT: {e}")
        return ""
