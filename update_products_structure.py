import pandas as pd
import os

DATA_FILE = "products.xlsx"

if os.path.exists(DATA_FILE):
    df = pd.read_excel(DATA_FILE)

    # Add new columns if they don't exist
    new_cols = {
        'Src_DeliveryReceipt': 1,
        'Src_Remaining': 1,
        'Src_Transfers': 1,
        'Src_Beverages': 1,
        'DR Price': 0.0
    }

    for col, default_val in new_cols.items():
        if col not in df.columns:
            df[col] = default_val

    # Save back
    df.to_excel(DATA_FILE, index=False)
    print("products.xlsx updated with new columns.")
    print(df.columns.tolist())
else:
    print("products.xlsx not found, creating new one.")
    df = pd.DataFrame(columns=["Business Name", "Product Category", "Product Name", "Price",
                               'Src_DeliveryReceipt', 'Src_Remaining', 'Src_Transfers', 'Src_Beverages', 'DR Price'])
    df.loc[0] = ["My Business", "General", "Sample Product", 100.00, 1, 1, 1, 1, 50.0]
    df.to_excel(DATA_FILE, index=False)
