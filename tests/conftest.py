# tests/conftest.py

import sys
import os

# Computing the project root (one level up from tests/)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Insert the project root at the front of sys.path, so "app" and "src" can be imported
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
