import os
import sys
from ultralytics import YOLO
from src.exception.exception import CustomException
from src.logger.logger import logging

class Detect:
    def __init__(self, model_path = 'models/yolov8n.pt'):
        try:
            if not os.path.exists(model_path):
                raise FileNotFoundError(f'Model not found at {model_path}')
            
            self.model = YOLO(model_path)
            logging.info(f'Model loaded from {model_path}')
        except Exception as e:
            logging.exception('Failed to initialize model')
            raise CustomException(e, sys)

    def predict(self, image_path):
        try:
            results = self.model.predict(image_path)
            logging.info('Prediction done')
            return results
        except Exception as e:
            logging.exception('Failed to predict')
            raise CustomException(e, sys)