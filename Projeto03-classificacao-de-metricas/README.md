# 📘 Desafio 3 – Métricas de Avaliação em Classificação

## 🎯 Objetivo
Implementar um programa em Python para calcular as principais métricas utilizadas na avaliação de modelos de classificação de dados.  
As métricas a serem calculadas são:

- **Acurácia**
- **Sensibilidade (Recall)**
- **Especificidade**
- **Precisão**
- **F-Score**

---

## 📊 Fundamentação
As métricas são baseadas nos valores da **matriz de confusão**, que pode ser definida de forma arbitrária para fins de estudo.  

- **VP (Verdadeiros Positivos)**: casos corretamente classificados como positivos.  
- **VN (Verdadeiros Negativos)**: casos corretamente classificados como negativos.  
- **FP (Falsos Positivos)**: casos incorretamente classificados como positivos.  
- **FN (Falsos Negativos)**: casos incorretamente classificados como negativos.  

---

## 🧮 Fórmulas (Tabela 1)

| Métrica            | Fórmula                                  |
|--------------------|-------------------------------------------|
| **Acurácia**       | (VP + VN) / (VP + VN + FP + FN)           |
| **Sensibilidade**  | VP / (VP + FN)                           |
| **Especificidade** | VN / (VN + FP)                           |
| **Precisão**       | VP / (VP + FP)                           |
| **F-Score**        | 2 × (Precisão × Sensibilidade) / (Precisão + Sensibilidade) |

---

## ⚙️ Implementação
O programa foi implementado em **Python puro**, recebendo como entrada os valores de **VP, VN, FP e FN**, e calculando todas as métricas automaticamente.

Exemplo de trecho de código:

```python
VP = 50
VN = 40
FP = 5
FN = 5

acuracia = (VP + VN) / (VP + VN + FP + FN)
sensibilidade = VP / (VP + FN)
especificidade = VN / (VN + FP)
precisao = VP / (VP + FP)
fscore = 2 * (precisao * sensibilidade) / (precisao + sensibilidade)

print("Acurácia:", acuracia)
print("Sensibilidade:", sensibilidade)
print("Especificidade:", especificidade)
print("Precisão:", precisao)
print("F-Score:", fscore)
```

---

## ▶️ Como executar
1. Clone este repositório ou baixe os arquivos.  
2. Abra o terminal na pasta do projeto.  
3. Execute o script em Python:  
   ```bash
   python desafio3_metricas.py
   ```  
4. O resultado das métricas será exibido no console.

---

## ✅ Exemplo de saída
```
Acurácia: 0.90
Sensibilidade: 0.91
Especificidade: 0.88
Precisão: 0.91
F-Score: 0.91
```

---

## 📂 Estrutura do Repositório
```
desafio3/
│── desafio3_metricas.py   # Script principal
│── README.md              # Documentação do projeto
```

---

## 📌 Observação
A matriz de confusão pode ser escolhida livremente, pois o objetivo deste desafio é **compreender o funcionamento das métricas** e não avaliar um modelo real.  