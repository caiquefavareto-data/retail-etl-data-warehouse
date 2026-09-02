import pandas as pd
import logging

def extract_data():
    logging.info("Lendo arquivo CSV do sistema legado (ERP)...")
    # Lê os dados brutos da pasta data/raw
    df = pd.read_csv('data/raw/sales_erp.csv')
    return df
