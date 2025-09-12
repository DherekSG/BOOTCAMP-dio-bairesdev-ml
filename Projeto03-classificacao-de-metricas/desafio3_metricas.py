# desafio3_metricas.py
# Calcula métricas de classificação a partir de VP, VN, FP, FN.

def safe_div(a, b):
    return a / b if b != 0 else 0.0

def sensibilidade(VP, FN):
    # Recall = VP / (VP + FN)
    return safe_div(VP, VP + FN)

def especificidade(VN, FP):
    # Specificity = VN / (FP + VN)
    return safe_div(VN, FP + VN)

def acuracia(VP, VN, FP, FN):
    # Accuracy = (VP + VN) / N
    N = VP + VN + FP + FN
    return safe_div(VP + VN, N)

def precisao(VP, FP):
    # Precision = VP / (VP + FP)
    return safe_div(VP, VP + FP)

def fscore(prec, rec):
    # F1 = 2 * (P * S) / (P + S)
    return safe_div(2 * (prec * rec), (prec + rec))

def calcular_metricas(VP, VN, FP, FN):
    rec = sensibilidade(VP, FN)
    spe = especificidade(VN, FP)
    acc = acuracia(VP, VN, FP, FN)
    pre = precisao(VP, FP)
    f1  = fscore(pre, rec)
    return {
        "sensibilidade": rec,
        "especificidade": spe,
        "acuracia": acc,
        "precisao": pre,
        "f1_score": f1,
    }

if __name__ == "__main__":
    # 👉 troque estes valores pelo da sua matriz de confusão
    VP, VN, FP, FN = 50, 40, 5, 5

    m = calcular_metricas(VP, VN, FP, FN)
    print(f"VP={VP} VN={VN} FP={FP} FN={FN}")
    for k, v in m.items():
        print(f"{k}: {v:.4f}")
