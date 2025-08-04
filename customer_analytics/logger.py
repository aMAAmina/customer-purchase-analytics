import logging
import os

_logger = None

def get_logger():
    global _logger
    if _logger is None:
        _logger = logging.getLogger("customer_analytics")
        _logger.setLevel(logging.INFO)
        os.makedirs("reports", exist_ok=True)
        handler = logging.StreamHandler("reports/pipeline.log")
        formatter = logging.Formatter('%(asctime)s %(levelname)s:%(message)s')
        handler.setFormatter(formatter)
        _logger.addHandler(handler)
        _logger.propagate = False
    return _logger