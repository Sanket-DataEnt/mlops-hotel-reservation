import os
import pandas
from src.logger import get_logger
from src.custom_exception import CustomException
import yaml

logger = get_logger(__name__)

# Function to read YAML file
def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File is not in a given path : {file_path}")
        
        with open(file_path, "r") as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info("Successfully read the YAML file")
            return config
    
    except Exception as e:
        logger.error(f"Error reading YAML file: {e}")
        raise CustomException(f"Failed to read YAML file: {e}")

