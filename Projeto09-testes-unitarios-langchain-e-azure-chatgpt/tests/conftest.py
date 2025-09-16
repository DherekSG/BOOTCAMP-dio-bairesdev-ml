# tests/conftest.py
import os
import sys

# adiciona a pasta do projeto e a pasta examples ao PYTHONPATH do pytest
sys.path.append(os.path.abspath("."))           # raiz do projeto
sys.path.append(os.path.abspath("./examples"))  # permite: import math_utils
