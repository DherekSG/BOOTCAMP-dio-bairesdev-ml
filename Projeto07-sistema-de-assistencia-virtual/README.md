# 🤖 Sistema de Assistência Virtual (Projeto 07 - Bootcamp DIO)

Este projeto implementa um **sistema de assistência virtual do zero**, utilizando **Processamento de Linguagem Natural (PLN)** em Python.  
O assistente é capaz de **ouvir comandos de voz, processar o texto e executar ações automatizadas**, além de responder utilizando síntese de voz (TTS).

---

## 📌 Funcionalidades

- 🎤 **Reconhecimento de fala (STT - Speech to Text)**  
  Converte sua fala em texto usando a biblioteca `speech_recognition`.

- 🔊 **Síntese de voz (TTS - Text to Speech)**  
  Responde em áudio utilizando a biblioteca `pyttsx3`.

- ⚙️ **Execução de comandos automatizados por voz**  
  - **"Abrir YouTube"** → abre o site do YouTube  
  - **"Abrir Wikipedia"** → abre a Wikipedia  
  - **"Farmácia perto de mim"** → pesquisa no Google Maps  
  - **"Sair" ou "Parar"** → encerra o assistente  

---

## 🛠️ Tecnologias Utilizadas

- [Python 3.11+](https://www.python.org/)
- [speech_recognition](https://pypi.org/project/SpeechRecognition/) → Conversão de fala em texto
- [pyttsx3](https://pypi.org/project/pyttsx3/) → Conversão de texto em fala
- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) → Captura de áudio do microfone
- [webbrowser](https://docs.python.org/3/library/webbrowser.html) → Abertura de páginas da web

---

## 📂 Estrutura de Pastas

```bash
Projeto07-sistema-de-assistencia-virtual/
│
├── src/
│   ├── assistant.py   # Arquivo principal do assistente
│   ├── stt.py         # Módulo de reconhecimento de fala (Speech-to-Text)
│   ├── tts.py         # Módulo de síntese de voz (Text-to-Speech)
│
├── requirements.txt   # Dependências do projeto
└── README.md          # Documentação do projeto
```

---

## ⚙️ Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/Projeto07-sistema-de-assistencia-virtual.git
   cd Projeto07-sistema-de-assistencia-virtual
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate  # Linux/Mac
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Como Executar

1. Certifique-se de que seu **microfone está funcionando**.  
2. No diretório `src/`, execute:
   ```bash
   python assistant.py
   ```
3. Fale um dos comandos de voz:
   - **"Abrir YouTube"**
   - **"Abrir Wikipedia"**
   - **"Farmácia perto de mim"**
   - **"Sair"** ou **"Parar"** para encerrar

---

## 📋 Exemplo de Uso

```bash
🗣️  Assistente iniciado. Diga um comando quando estiver pronto.
🎙️  Fale seu comando...
✅ Você disse: abrir youtube
🔊 Assistente: Abrindo YouTube
```

---

## 📦 requirements.txt

```txt
speechrecognition
pyttsx3
pyaudio
```

---

## 🚀 Melhorias Futuras

- Integração com APIs externas (clima, notícias, música).
- Controle de dispositivos IoT por voz.
- Personalização de respostas com IA.

---

👨‍💻 Desenvolvido como parte do **Bootcamp DIO - BairesDev Machine Learning**.