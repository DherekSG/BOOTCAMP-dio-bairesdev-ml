# 🤖 Projeto 09 – Agente de Testes Unitários com LangChain + Azure OpenAI

Este projeto faz parte do **Bootcamp DIO + BairesDev (Machine Learning)** e tem como objetivo implementar um **agente em Python** capaz de **gerar automaticamente testes unitários em pytest** a partir de código Python fornecido.  

O agente utiliza:
- **LangChain** para orquestração da LLM,
- **Azure OpenAI** como modelo de linguagem,
- **pytest** para execução dos testes.

---

## 📌 Objetivos de Aprendizado
- Entender como integrar **LangChain** com **Azure OpenAI**.  
- Criar um **agente autônomo** que gera testes unitários a partir de código-fonte.  
- Praticar **engenharia de prompts** para instruir a IA a produzir código de testes válido.  
- Automatizar a validação de código com **pytest**.  

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.11+**
- [LangChain](https://www.langchain.com/)
- [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/)
- [pytest](https://docs.pytest.org/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 📂 Estrutura do Projeto

```bash
Projeto09-testes-unitarios-langchain-e-azure-chatgpt/
│── agent/
│   ├── __init__.py
│   ├── agent.py        # Lógica principal do agente
│   └── main.py         # CLI para gerar testes
│── examples/
│   └── math_utils.py   # Funções simples para exemplo
│── tests/
│   └── test_math_utils.py  # Arquivo de testes gerado automaticamente
│── .env                # Variáveis de ambiente (não versionar)
│── .env.example        # Exemplo de configuração
│── requirements.txt    # Dependências do projeto
│── README.md           # Documentação do projeto
```

---

## ⚙️ Configuração do Ambiente

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/Projeto09-testes-unitarios-langchain-e-azure-chatgpt.git
cd Projeto09-testes-unitarios-langchain-e-azure-chatgpt
```

### 2. Criar e ativar ambiente virtual
```powershell
python -m venv venv
.env\Scriptsctivate
```

### 3. Instalar dependências
```powershell
pip install -r requirements.txt
pip install -U openai langchain-openai langchain-core pytest python-dotenv
```

### 4. Configurar variáveis de ambiente
Crie um arquivo **`.env`** na raiz do projeto com as informações do **Azure OpenAI**:

```env
AZURE_OPENAI_ENDPOINT=https://bootcampdio.openai.azure.com/
AZURE_OPENAI_API_KEY=SUA_CHAVE_AQUI
AZURE_OPENAI_API_VERSION=2024-12-01-preview
AZURE_OPENAI_DEPLOYMENT=o4-mini
```

> ⚠️ Não versionar o arquivo `.env`. Use `.env.example` para compartilhar estrutura de configuração.

---

## ▶️ Uso do Agente

### Gerar testes para um arquivo
```powershell
python -m agent.main --input examples\math_utils.py --output tests\test_math_utils.py
```

Saída esperada:
```
Arquivo de testes gerado em: tests\test_math_utils.py
```

### Executar os testes
```powershell
python -m pytest -q
```

Saída esperada:
```
........
8 passed in 0.27s
```

---

## 🧩 Exemplo

### Código de entrada – `examples/math_utils.py`
```python
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não permitida.")
    return a / b
```

### Código de saída gerado – `tests/test_math_utils.py`
```python
import pytest
from examples.math_utils import add, divide

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_divide_valid():
    assert divide(10, 2) == 5

def test_divide_zero_division():
    with pytest.raises(ValueError):
        divide(10, 0)
```

---

## 🚀 Próximos Passos
- Gerar testes para outros arquivos em `examples/`.  
- Ajustar o agente para cenários mais complexos.  
- Integrar em um pipeline **CI/CD (GitHub Actions)** para rodar os testes automaticamente.  

---

## 👨‍💻 Autor
Projeto desenvolvido por **Dherek Schaberle** no **Bootcamp DIO + BairesDev**, com apoio do **Azure OpenAI**.  

---