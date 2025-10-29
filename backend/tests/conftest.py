import sys
import os

# Caminho absoluto até a pasta backend/
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Garante que o diretório backend/ esteja no sys.path
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
