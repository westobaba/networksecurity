import logging
import os
from datetime import datetime

# Define the directory and file path
logs_dir = 'logs'
os.makedirs(logs_dir, exist_ok=True)

log_file_name = f"{datetime.now().strftime('%Y-%m-%d_%H')}.log"
log_file_path = os.path.join(logs_dir, log_file_name)

# Create a custom logger instance instead of using basicConfig
logger = logging.getLogger("networksecurity_logger")
logger.setLevel(logging.INFO)

# Create a file handler and set the formatter
file_handler = logging.FileHandler(log_file_path)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))

# Add the handler to the logger
logger.addHandler(file_handler)