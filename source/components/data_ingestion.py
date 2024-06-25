##  Data Ingestion  ##

import os
import sys
from source.exception import CustomException
from source.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from source.components.data_transformation import DataTransformation
from source.components.data_transformation import DataTransformationConfig

@dataclass       ## Using this we can directly define class variables. i.e. without using __init__
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')
    
    # This class tells where to save the train path, test path, and raw data path. 
    
class dataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
            
    def initiate_data_ingestion(self):
        ## If data is stored in databases, we have to write some code to get that data
        logging.info("Entered The data ingestion method or component")
        try:
            df = pd.read_csv('notebook/data/student.csv')
            logging.info('Read the dataset as dataframe') 
                
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok = True)
                
            df.to_csv(self.ingestion_config.raw_data_path, index = False, header=True)
                
            logging.info('Train Test Split Initiated')
                
            train_set, test_set = train_test_split(df, test_size = 0.2, random_state=42)
                
            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)
                
            logging.info('Data Ingestion Completed')
                
            return(
                    self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path
                )
                
        except Exception as e:
            raise CustomException(e, sys) 
            
            
if __name__=='__main__':
    obj = dataIngestion()
    train_data, test_data = obj.initiate_data_ingestion() 
    
    
    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)
         