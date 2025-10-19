import os
import sys
import pandas as pd
from google.cloud import storage
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self, config):
        self.config = config["data_ingestion"]
        self.bucket_name = self.config["bucket_name"]
        self.file_names = self.config["bucket_file_names"]

        os.makedirs(RAW_DIR, exist_ok=True)

        logger.info(f"DataIngestion initialized with bucket: {self.bucket_name} and files: {self.file_names}")
    
    def download_csv_from_gcp(self):
        try:
            client = storage.Client()
            bucket = client.bucket(self.bucket_name)

            for file_name in self.file_names:
                file_path = os.path.join(RAW_DIR, file_name)

                if file_name == "animelist.csv":
                    blob = bucket.blob(file_name)
                    blob.download_to_filename(file_path)

                    data = pd.read_csv(file_path, nrows=500000)
                    data.to_csv(file_path, index=False)
                    logger.info("Downloaded and truncated animelist.csv to 500,000 rows")
                else:
                    blob = bucket.blob(file_name)
                    blob.download_to_filename(file_path)
                    logger.info(f"Downloaded {file_name} from GCP bucket {self.bucket_name} to {file_path}")
        except Exception:
            logger.error("Error occurred while downloading files from GCP")
            raise CustomException("Failed to download files from GCP", sys)
    
    def run(self):
        try:
            logger.info("Data ingestion process started")
            self.download_csv_from_gcp()
            logger.info("Data ingestion process completed")
        except Exception:
            logger.error("Error in data ingestion process")
            raise CustomException("Data ingestion process failed", sys)
        finally:
            logger.info("Exiting DataIngestion.run method")

if __name__ == "__main__":
    try:
        config = read_yaml(CONFIG_PATH)
        data_ingestion = DataIngestion(config)
        data_ingestion.run()
    except Exception:
        logger.error("Error in main execution")
        raise CustomException("Main execution failed", sys)
