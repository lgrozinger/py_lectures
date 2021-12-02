try:
  import tellurium as te
except ImportError:
  import os
  os.system("python -m pip install --upgrade pip")
  os.system("python -m pip install tellurium")

try:
  import seaborn
except ImportError:
  os.system("python -m pip install seaborn")