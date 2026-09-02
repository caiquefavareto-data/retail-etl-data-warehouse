import pandas as pd
import logging

def clean_data(df):
    logging.info("Limpando dados: removendo nulos e calculando o total...")
    
    # 1. Remove qualquer linha que tenha dados vazios/nulos (como a linha 3 e 4 do nosso CSV)
    df_clean = df.dropna().copy()
    
    # 2. Cria uma nova coluna calculando o Valor Total (Quantidade * Preço)
    df_clean['total_amount'] = df_clean['qty'] * df_clean['price']
    
    return df_clean
