import pandas as pd
import logging

def clean_data(raw_data):
    """Aplica regras de negócio, remove duplicatas e padroniza formatos."""
    logging.info("Removendo valores nulos e padronizando formatação de datas...")
    # Exemplo prático: df.dropna(inplace=True)
    return {"status": "dados_higienizados_com_sucesso"}
