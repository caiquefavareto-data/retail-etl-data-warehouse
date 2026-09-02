import sqlite3
import logging

def load_to_dw(df_clean):
    logging.info("Criando banco de dados local e carregando os dados...")
    
    # Conecta (ou cria) um banco de dados local chamado retail_dw.db
    conn = sqlite3.connect('retail_dw.db')
    
    # Salva os dados limpos direto em uma tabela SQL chamada Fact_Sales
    df_clean.to_sql('Fact_Sales', conn, if_exists='replace', index=False)
    
    conn.close()
    logging.info("Dados carregados com sucesso na Fact_Sales!")
