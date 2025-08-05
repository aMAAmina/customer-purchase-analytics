import logging
import os

_logger = None

def get_logger():
    global _logger
    if _logger is None:
        _logger = logging.getLogger("customer_analytics")
        _logger.setLevel(logging.INFO)
        os.makedirs("reports", exist_ok=True)
        file_handler = logging.FileHandler("reports/pipeline.log")
        formatter = logging.Formatter('%(asctime)s %(levelname)s:%(message)s')
        file_handler.setFormatter(formatter)
        _logger.addHandler(file_handler)
        _logger.propagate = False
    return _logger