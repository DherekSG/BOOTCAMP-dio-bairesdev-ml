from stt import transcribe_ptbr
from tts import speak
from intents import handle_intent

def main():
    speak("Assistente iniciado. Diga um comando quando estiver pronto.")
    while True:
        text = transcribe_ptbr()
        if not text:
            speak("Não entendi. Pode repetir?")
            continue
        response, should_exit = handle_intent(text)
        speak(response)
        if should_exit:
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        speak("Encerrando. Até logo.")
