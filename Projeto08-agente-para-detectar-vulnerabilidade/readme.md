# Projeto 08 – Agente para Detectar Vulnerabilidades 🔐

## 📌 Descrição
Este projeto foi desenvolvido como parte do **Bootcamp BairesDev – Machine Learning com a DIO**.  
O objetivo é criar uma **API em Python com FastAPI integrada ao Azure OpenAI**, capaz de:

- Receber uma **imagem** contendo o desenho de arquitetura de uma aplicação;  
- Processar essa imagem com **técnicas de Prompt Engineering**;  
- Gerar automaticamente uma **análise de ameaças** baseada na metodologia **STRIDE**:  
  - **S**poofing (Falsificação)  
  - **T**ampering (Adulteração)  
  - **R**epudiation (Repúdio)  
  - **I**nformation Disclosure (Divulgação de informações)  
  - **D**enial of Service (Negação de serviço)  
  - **E**levation of Privilege (Elevação de privilégio)  

---

## 🎯 Objetivos de Aprendizagem
- Aplicar conceitos de **Segurança da Informação** em ambiente prático;  
- Utilizar **Python + FastAPI** para expor uma API;  
- Experimentar a integração com **Azure OpenAI**;  
- Documentar e compartilhar a experiência no GitHub;  
- Demonstrar **capacidade de análise de riscos** baseada em metodologias reconhecidas.  

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.10+**  
- **FastAPI** (Framework para APIs)  
- **Azure OpenAI** (Modelos de IA)  
- **Uvicorn** (Servidor ASGI)  
- **Pydantic** (Validação de dados)  

---

## 📂 Estrutura do Projeto
```bash
Projeto08-agente-para-detectar-vulnerabilidade/
│
├── backend/
│   ├── main.py          # Código principal da API
│   ├── .env
│
├── frontend/
│   ├── index.html          # HTML Principal
│
├── .gitignore 
├── requirements.txt     # Dependências do projeto
└── README.md            # Documentação
```

---

## ▶️ Como Executar
### 1. Clonar o repositório
```bash
git clone https://github.com/DherekSG/BOOTCAMP-dio-bairesdev-ml.git
cd Projeto08-agente-para-detectar-vulnerabilidade
```

### 2. Criar ambiente virtual
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Rodar a API
```bash
uvicorn app.main:app --reload
```

Acesse em: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  

---

## 📊 Exemplo de Uso
1. Enviar uma **imagem de arquitetura** via endpoint `/analisar-arquitetura`.  
2. A API processa a entrada e retorna uma **análise STRIDE** semelhante a:  

```json
{
  "spoofing": "Risco de falsificação de identidade em autenticação sem MFA.",
  "tampering": "Dados em trânsito não possuem criptografia forte.",
  "repudiation": "Não há logs de auditoria configurados.",
  "information_disclosure": "Banco exposto em rede pública.",
  "denial_of_service": "Ausência de balanceamento de carga.",
  "elevation_of_privilege": "Contas de administrador sem segregação."
}
```

---

## 🧩 Reflexão
Este desafio foi importante para consolidar conceitos de:  
- **Cibersegurança aplicada** (STRIDE em arquiteturas reais);  
- **Integração de IA com desenvolvimento de APIs**;  
- **Documentação técnica** para portfólio.  

--- 
