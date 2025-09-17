import webbrowser
from urllib.parse import quote_plus
from datetime import datetime
import os
import sys

def open_default(url: str):
    try:
        webbrowser.open(url, new=2)  # new=2 tenta nova aba
        return True, None
    except Exception as e:
        return False, str(e)

def handle_intent(user_text: str):
    """
    Recebe texto em PT-BR e retorna (resposta_falada, encerra?).
    Executa ações: YouTube, Wikipedia, Maps (farmácia perto), abrir navegador, horas, parar.
    """
    t = user_text.lower()

    # sair
    if any(k in t for k in ["parar", "encerrar", "fechar assistente", "tchau"]):
        return "Encerrando. Até mais!", True

    # que horas são
    if "que horas" in t or "horas são" in t:
        now = datetime.now().strftime("%H:%M")
        return f"Agora são {now}.", False

    # abrir youtube
    if "abrir youtube" in t or "open youtube" in t:
        ok, err = open_default("https://www.youtube.com")
        return ("Abrindo YouTube." if ok else f"Não consegui abrir o YouTube: {err}"), False

    # abrir navegador / abrir chrome
    if "abrir navegador" in t or "abrir chrome" in t or "open chrome" in t:
        # Abre uma aba em branco (ou sua home)
        ok, err = open_default("about:blank")
        return ("Abrindo navegador." if ok else f"Não consegui abrir o navegador: {err}"), False

    # pesquisar wikipedia sobre X
    if "pesquisar no wikipedia" in t or "pesquisar wikipedia" in t or "wikipedia" in t:
        # tenta extrair o tópico depois de "sobre" ou após a palavra wikipedia
        topic = t
        for key in ["pesquisar no wikipedia", "pesquisar wikipedia", "wikipedia"]:
            topic = topic.replace(key, "")
        for key in ["sobre", "sobre o", "sobre a", "sobre os", "sobre as"]:
            topic = topic.replace(key, "")
        topic = topic.strip()
        if not topic:
            return "Diga o que deseja pesquisar no Wikipedia.", False
        url = f"https://pt.wikipedia.org/wiki/{quote_plus(topic)}"
        ok, err = open_default(url)
        return (f"Abrindo Wikipedia sobre {topic}." if ok else f"Não consegui abrir o Wikipedia: {err}"), False

    # farmácia mais próxima (Maps)
    if "farmácia" in t or "farmacia" in t:
        # O Google Maps vai usar a localização do navegador (se permitida)
        url = "https://www.google.com/maps/search/farmacia+perto+de+mim/"
        ok, err = open_default(url)
        return ("Mostrando farmácias próximas no Google Maps." if ok else f"Não consegui abrir o Google Maps: {err}"), False

    # pesquisa geral (extra)
    if t.startswith("pesquisar ") or t.startswith("buscar "):
        query = t.split(" ", 1)[1] if " " in t else ""
        if not query:
            return "Diga o que deseja pesquisar.", False
        url = f"https://www.google.com/search?q={quote_plus(query)}"
        ok, err = open_default(url)
        return (f"Pesquisando por {query} no Google." if ok else f"Não consegui abrir a pesquisa: {err}"), False

    # fallback
    return "Comando não reconhecido. Exemplos: abrir YouTube, pesquisar no Wikipedia sobre inteligência artificial, farmácia mais próxima, que horas são, parar.", False
