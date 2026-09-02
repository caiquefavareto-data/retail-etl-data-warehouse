import logging
from extract import extract_data
from transform import clean_data
from load import load_to_dw

def run_etl_pipeline():
    logging.info("--- INICIANDO PIPELINE ETL ---")
    
    raw_data = extract_data()
    processed_data = clean_data(raw_data)
    load_to_dw(processed_data)
    
    logging.info("--- PIPELINE CONCLUÍDO COM SUCESSO ---")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    run_etl_pipeline()
