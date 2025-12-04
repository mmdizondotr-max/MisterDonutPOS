import pandas as pd
import os

DATA_FILE = "products.xlsx"

if os.path.exists(DATA_FILE):
    df = pd.read_excel(DATA_FILE)
    print("Columns:", df.columns.tolist())
    print(df.head())
else:
    print(f"{DATA_FILE} not found")
