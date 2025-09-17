# Projeto: Treinamento de Rede YOLO para Detecção de Objetos

Este projeto tem como objetivo **treinar e avaliar uma rede YOLO** (You Only Look Once) utilizando o Google Colab e o dataset **COCO128** (versão reduzida do COCO).  
Também é possível testar o modelo em **imagens próprias**.

---

## 🚀 Estrutura do Projeto

```bash
Projeto-YOLO/
│
│── yolov8.ipynb           # Notebook principal no Google Colab
│── requirements.txt       # Dependências do projeto
│── README.md              # Documentação do projeto
```

---

## 📦 Dependências

Todas as dependências necessárias estão listadas em [`requirements.txt`](requirements.txt).  
As principais são:

- [Python 3.10+](https://www.python.org/)  
- [Ultralytics (YOLOv8)](https://github.com/ultralytics/ultralytics)  
- [PyTorch](https://pytorch.org/) (com suporte CUDA no Colab)  
- [Google Colab](https://colab.research.google.com/) (opcional, mas recomendado para uso de GPU)

---

## 🧭 Rotas do Projeto

O projeto foi dividido em **três rotas principais**:

### 🔹 Rota A – Treinamento do Modelo

```python
from ultralytics import YOLO
import glob, os

# Carregar modelo base YOLOv8 nano (rápido)
model = YOLO('yolov8n.pt')

# Treinar no COCO128
results = model.train(
    data='coco128.yaml',
    epochs=10,
    imgsz=640,
    batch=16,
    device=0  # usa GPU no Colab
)

# Caminhos do melhor modelo
exp_dir = sorted(glob.glob('runs/detect/train*'))[-1]
best = os.path.join(exp_dir, 'weights', 'best.pt')
print("EXP_DIR:", exp_dir)
print("BEST:", best)
```

---

### 🔹 Rota B – Avaliação e Predição no Dataset

```python
# Carregar melhor modelo treinado
infer_model = YOLO(best)

# Definir pasta de validação
candidates = [
    "/content/datasets/coco128/images/val",
    "/content/datasets/coco128/images/val2017",
    "/content/datasets/coco128/images/train"
]
val_dir = next((p for p in candidates if os.path.exists(p)), None)

print("Usando para predição:", val_dir)

# Rodar predição
pred = infer_model.predict(source=val_dir, imgsz=640, conf=0.25, save=True)

# Listar imagens geradas
!ls -la runs/detect/predict*/ | head -n 20
```

---

### 🔹 Rota C – Testar em Imagens Próprias

```python
from google.colab import files
import shutil, glob
from IPython.display import Image, display

# Criar pasta para imagens próprias
!mkdir -p /content/my_images

# Upload de imagens
uploaded = files.upload()
for filename in uploaded.keys():
    shutil.move(filename, "/content/my_images/" + filename)

# Rodar predição nas imagens do usuário
pred = infer_model.predict(source="/content/my_images", imgsz=640, conf=0.25, save=True)

# Mostrar primeiros resultados
result_imgs = glob.glob("runs/detect/predict*/**.jpg", recursive=True)
for img_path in result_imgs[:5]:
    display(Image(filename=img_path, width=600))
```

---

## 📊 Resultados Esperados

Após o treinamento e as predições, você verá algo assim:

- 🚲 **bicicleta**  
- 🐕 **cachorro**  
- 🚗 **carro**  
- **ETC ....**

Com bounding boxes coloridas em cada objeto detectado.

---

## 📊 Resultados do Projeto

Após o treinamento, o modelo YOLOv8 foi utilizado para detectar objetos em imagens de teste.
As imagens de saída geradas pelo modelo foram salvas na pasta /images do projeto.


## 📌 Observações

- O **dataset COCO128** é usado apenas para demonstração (leve).  
- Para projetos reais, use o **COCO completo** ou crie seu próprio dataset anotado.  
- O treinamento pode ser expandido para **50+ epochs** se usar GPU com maior poder.  

---

## 👨‍💻 Autor

Projeto desenvolvido durante o Bootcamp da **DIO + BairesDev**  
Implementação prática por **Dherek Schaberle** 🚀