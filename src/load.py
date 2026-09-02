import logging

def load_to_dw(processed_data):
    """Carrega os dados finais no Data Warehouse respeitando o Star Schema."""
    logging.info("Inserindo registros nas tabelas Dim_Product, Dim_Store, Dim_Date e Fact_Sales...")
    # Exemplo prático: df.to_sql('Fact_Sales', con=engine, if_exists='append')
    return True
