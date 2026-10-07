import pandas as pd
import sklearn
from dotenv import load_dotenv

print("Python OK")
print("Pandas :", pd.__version__)
print("Scikit-learn :", sklearn.__version__)
print("Environnement MLOps OK")
import os

load_dotenv()

api_key = os.getenv("API_KEY")

print("API_KEY chargée :", api_key)