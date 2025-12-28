import pandas as pd
import os

DATA_FILE = "products.xlsx"

if os.path.exists(DATA_FILE):
    df = pd.read_excel(DATA_FILE)

    # 1. Remove obsolete columns
    cols_to_remove = ["Src_Remaining", "Src_Transfers"]
    existing_cols = [c for c in cols_to_remove if c in df.columns]

    if existing_cols:
        df.drop(columns=existing_cols, inplace=True)
        print(f"Removed columns: {existing_cols}")

    # 2. Add missing required columns
    required_defaults = {
        'Src_DeliveryReceipt': 0,
        'Src_O_Beverages': 0,
        'DR Price': 0.0
    }

    added_cols = []
    for col, default_val in required_defaults.items():
        if col not in df.columns:
            df[col] = default_val
            added_cols.append(col)

    if added_cols:
        print(f"Added missing columns: {added_cols}")

    if existing_cols or added_cols:
        df.to_excel(DATA_FILE, index=False)
        print("products.xlsx updated.")
    else:
        print("products.xlsx structure is already up to date.")

    print("Current columns:", df.columns.tolist())

else:
    print("products.xlsx not found, creating new one.")
    req_cols = ["Business Name", "Product Category", "Product Name", "Price",
                    "Src_DeliveryReceipt", "Src_O_Beverages", "DR Price"]
    df = pd.DataFrame(columns=req_cols)
    df.loc[0] = ["My Business", "General", "Sample Product", 100.00, 1, 0, 50.0]
    df.to_excel(DATA_FILE, index=False)
    print("Created new products.xlsx with streamlined structure.")
