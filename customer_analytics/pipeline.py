from customer_analytics.ingestion import ingest
from customer_analytics.transformation import transform

def run_pipeline(datapath=None, chunksize=None):
    df_iter = ingest(datapath, chunksize=chunksize)
    transform(df_iter)