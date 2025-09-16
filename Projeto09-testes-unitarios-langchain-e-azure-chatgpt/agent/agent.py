"""
Agente gerador de testes unitários com pytest usando LangChain + Azure OpenAI.

- Usa AzureChatOpenAI (cliente correto para Azure) via langchain-openai.
- Carrega variáveis do .env automaticamente com python-dotenv.

Como usar (CLI):
    python -m agent.main --input examples/math_utils.py --output tests/test_math_utils.py

Como usar (em código):
    from agent.agent import generate_tests_for_code
    tests_py = generate_tests_for_code(open("examples/math_utils.py").read(), module_name="math_utils")
"""

import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Carrega variáveis do arquivo .env na raiz do projeto (se existir)
load_dotenv()

SYSTEM_PROMPT = (
    "Você é um gerador de testes unitários profissional. "
    "Receberá um arquivo/trecho de código Python e deve produzir APENAS um arquivo de testes pytest válido. "
    "REGRAS OBRIGATÓRIAS:\n"
    "1) A PRIMEIRA linha do arquivo de saída DEVE ser: 'import pytest'\n"
    "2) Escreva funções de teste com nomes começando por 'def test_'\n"
    "3) Cubra cenários de SUCESSO e de FALHA (quando aplicável)\n"
    "4) Não inclua comentários extensos, prints ou texto fora do Python\n"
    "5) Se o módulo tiver docstrings com exemplos, transforme em asserts\n"
    "6) Não invente importações do projeto; importe apenas o módulo sob teste"
)

USER_PROMPT_TMPL = (
    "Gere testes pytest para o seguinte código Python.\n"
    "Nome do módulo sob teste: {module_name}\n\n"
    "<<<CÓDIGO PYTHON>>>\n"
    "{code}\n"
    "<<<FIM>>>\n\n"
    "IMPORTANTE: retorne somente o conteúdo do arquivo de testes."
)

def _get_llm() -> AzureChatOpenAI:
    """
    Instancia um cliente AzureChatOpenAI com base nas variáveis de ambiente.

    Necessárias:
      - AZURE_OPENAI_ENDPOINT (e.g., https://SEU-RECURSO.openai.azure.com/)
      - AZURE_OPENAI_API_KEY
      - AZURE_OPENAI_DEPLOYMENT  (NOME do deployment criado no portal)
    Opcionais:
      - AZURE_OPENAI_API_VERSION (padrão: 2024-02-15-preview)
    """
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    if not (endpoint and api_key and deployment):
        raise EnvironmentError(
            "Variáveis de ambiente ausentes. Configure AZURE_OPENAI_ENDPOINT, "
            "AZURE_OPENAI_API_KEY e AZURE_OPENAI_DEPLOYMENT (nome do deployment)."
        )

    # Cliente correto para Azure
    return AzureChatOpenAI(
    api_key=api_key,
    azure_endpoint=endpoint,
    api_version=api_version,
    azure_deployment=deployment,
    # sem temperature (ou deixe temperature=1)
)


def generate_tests_for_code(code: str, module_name: str = "module") -> str:
    """
    Gera o conteúdo (string) de um arquivo de testes pytest para o código fornecido.
    """
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            ("user", USER_PROMPT_TMPL),
        ]
    )
    chain = prompt | _get_llm() | StrOutputParser()
    return chain.invoke({"code": code, "module_name": module_name})

def generate_tests_for_file(input_path: str, module_name: Optional[str] = None) -> str:
    """
    Lê um arquivo .py e devolve a string com o conteúdo do teste.
    """
    with open(input_path, "r", encoding="utf-8") as f:
        code = f.read()
    if module_name is None:
        module_name = Path(input_path).stem
    return generate_tests_for_code(code, module_name=module_name)
