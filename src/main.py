import logging
from extract import extract_data
from transform import clean_data
from load import load_to_dw

def run_etl_pipeline():
    logging.info("Iniciando fase de Extração (Extract)...")
    raw_data = extract_data()
    
    logging.info("Iniciando higienização e padronização (Transform)...")
    processed_data = clean_data(raw_data)
    
    logging.info("Carregando no Data Warehouse - Star Schema (Load)...")
    load_to_dw(processed_data)
    
    logging.info("Pipeline ETL finalizado com sucesso.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    run_etl_pipeline()
