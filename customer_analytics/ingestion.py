from customer_analytics.utils import abs_ff_path
from customer_analytics.logger import get_logger
from customer_analytics.config import dev
import os
import pandas as pd

logger = get_logger()

def ingest(datapath=None, chunksize=None):
    logger.info("Ingestion starting...")
    if chunksize is None:
        chunksize = dev.CHUNKSIZE
    logger.info(f"Chunk data size: {chunksize}")

    raw_path = abs_ff_path("../data/raw/customer_purchases_large.csv")

    if datapath is None:
        datapath = dev.DATAPATH
    os.makedirs(datapath, exist_ok=True)
    logger.info(f"Data path of processed data: {datapath}")

    for chunk in pd.read_csv(raw_path, chunksize=chunksize, low_memory=False):
        yield chunk
    