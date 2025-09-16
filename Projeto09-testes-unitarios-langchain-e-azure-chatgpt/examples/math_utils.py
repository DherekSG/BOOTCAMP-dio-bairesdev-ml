"""
Funções simples para demonstração.
"""

def add(a: float, b: float) -> float:
    """Soma dois números."""
    return a + b

def divide(a: float, b: float) -> float:
    """Divide a por b. Lança ZeroDivisionError quando b == 0."""
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida.")
    return a / b
