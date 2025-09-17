import pyttsx3

_engine = None

def _get_engine():
    global _engine
    if _engine is None:
        _engine = pyttsx3.init()
        # Ajustes de voz/velocidade/volume (opcional)
        _engine.setProperty("rate", 180)   # velocidade
        _engine.setProperty("volume", 1.0) # 0.0 a 1.0
    return _engine

def speak(text: str):
    print(f"🗣️  {text}")
    engine = _get_engine()
    engine.say(text)
    engine.runAndWait()
