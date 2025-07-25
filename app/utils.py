import logging
from datetime import datetime

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', handlers=[logging.FileHandler(f'app_{datetime.now().date()}.log'), logging.StreamHandler()])
