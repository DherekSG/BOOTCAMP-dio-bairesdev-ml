# Sistema de Recomendação por Imagens (Desafio DIO)

> **Objetivo:** recomendar itens **visualmente semelhantes** usando apenas a **aparência** (cor, textura, formato), sem depender de dados textuais (marca, preço etc.).

- **Bootcamp / Módulo:** DIO — Machine Learning (Desafio de Recomendação por Imagens)
- **Notebook:** `./SistemadeRecomendacao.ipynb`


---

## 🧠 Visão Geral

Pipeline **content-based** (similaridade por conteúdo):

1. **Dataset** organizado em pastas por classe (ex.: `data/relogio`, `data/camiseta`, `data/sapato`…).
2. **Extração de características** com CNN pré-treinada (ex.: VGG16/EfficientNet, ImageNet, `include_top=False`, *pooling* global).
3. **Indexação & Busca** com KNN por **similaridade do cosseno** (FAISS ou `sklearn.neighbors`).
4. **Consulta:** dada uma imagem, retornamos os **Top-K** mais parecidos visualmente.

> O foco é a **aparência** — não usamos descrição, marca, preço ou outros metadados.

---

## 🗂️ Estrutura de Pastas (sugestão)

```
.
├─ data/                      # imagens (cada classe em uma pasta)
│  ├─ relogio/
│  ├─ camiseta/
│  └─ ...
├─ notebooks/
│  └─ SistemadeRecomendacao.ipynb
├─ artifacts/                 # gerados pelo notebook
│  ├─ embeddings.npy
│  ├─ paths.json
│  └─ faiss_index.ip         # se FAISS estiver disponível
└─ README.md
```

> **Dica:** ≥ 50 imagens por classe, com variedade de ângulos e iluminação.

---

## 🧰 Tecnologias

- Python 3.10+
- TensorFlow/Keras *(ou PyTorch/CLIP, se preferir)*
- FAISS **ou** `sklearn.neighbors` (KNN com métrica **cosine**)
- NumPy, Pillow, Matplotlib, tqdm
- (Opcional) Gradio para demo web

**`requirements.txt` (exemplo):**
```
tensorflow>=2.15
tensorflow-hub>=0.16.1
numpy
pandas
scikit-learn
faiss-cpu
Pillow
matplotlib
tqdm
gradio
```

---

## 🚀 Como Executar

### Opção A — Google Colab (zip local, sem Drive)
1. Compacte seu dataset como **`data.zip`** com a pasta `data/` na raiz:
   ```
   data/
     ├─ relogio/
     ├─ camiseta/
     └─ ...
   ```
2. Faça upload no Colab e extraia:
   ```python
   import shutil
   shutil.unpack_archive("data.zip", "/content/")
   ```
3. Aponte `DATA_DIR = "/content/data"` no notebook.
4. Rode as células: carregar dataset → extrair embeddings → indexar → consultar.

### Opção B — Ambiente Local (CPU/GPU)
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
# depois, rode o notebook em notebooks/SistemadeRecomendacao.ipynb
```

---

## 🔬 Metodologia

- **Pré-processamento:** redimensionamento (ex.: **224×224**), normalização conforme o backbone escolhido (ex.: `keras.applications.*.preprocess_input` ou `rescale=1./255`).
- **Backbone:** CNN pré-treinada no ImageNet (ex.: `VGG16(weights="imagenet", include_top=False, pooling="avg")` ou `EfficientNetB0`).
- **Embeddings:** vetor por imagem (pooling global), **L2-normalizado** para uso com **cosine similarity**.
- **Indexação/Busca:**
  - **FAISS** (`IndexFlatIP`) quando disponível (produto interno ≅ cosseno após L2-normalização);
  - *Fallback:* `NearestNeighbors(metric="cosine")` (scikit-learn).
- **Consulta:** Top-K vizinhos mais similares (opcional: filtrar recomendações pela mesma classe da consulta).

---

## 📏 Avaliação

Métrica simples sugerida: **Recall@K por classe**  
- Amostre imagens como consulta;  
- **Conta acerto** se ao menos um entre Top-K tem a **mesma classe** da consulta;  
- Reporte **Recall@1, @3, @5, @10**.

**Resultados (exemplo — substitua pelos seus):**
- Recall@1: **0.78**
- Recall@5: **0.92**
- Recall@10: **0.96**

> Se classes se confundirem (ex.: relógios de cores muito próximas), aumente o dataset, varie ângulos ou use um backbone mais forte (EfficientNetB3/CLIP).

---

## 📸 Exemplos de Resultados

Inclua prints com **QUERY** + **Top-K** retornos (títulos com *score* ajudam).  
- Ex.: *Consulta: relógio prateado → recomendações com mostrador/metal semelhantes.*

---

## ➕ Atualizando o Catálogo

1. Adicione novas imagens em `data/<classe>/...`;
2. Re-extraia embeddings (ou extraia só das novas e **concatene** aos existentes);
3. Recrie/atualize o índice FAISS/KNN;
4. Valide com algumas consultas.

---

## 🛠️ Troubleshooting

- **Aba travando no Colab**: evite mostrar galerias enormes; reduza `IMG_SIZE` (160–224) e `BATCH_SIZE` (8–16); salve em `/content/artifacts` e só depois copie para o Drive.
- **Execução lenta**: VGG16 é pesada; troque para EfficientNetB0/MobileNetV2 para acelerar.
- **“Nenhuma imagem encontrada”**: confira extensões suportadas (`.jpg .jpeg .png .bmp .webp`) e a estrutura `data/<classe>/*`.
- **Drive lento**: grave os artefatos em `/content/` durante o processamento e sincronize no final.

---

## 🗺️ Roadmap

- Índices FAISS IVF/IVFPQ para catálogos grandes;
- Re-ranking por cor (HSV) ou forma;
- UI com Gradio/Streamlit e filtros por categoria;
- API REST (FastAPI) para servir o modelo.

---

## 📚 Referências

- DIO — Desafio de Recomendação por Imagens
- Sparsh AI — *Image Similarity Recommendations* (Colab)  
- FAISS — Facebook AI Similarity Search
- Keras Applications (VGG/EfficientNet)

---