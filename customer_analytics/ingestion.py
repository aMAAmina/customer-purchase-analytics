from customer_analytics.utils import *
import pandas as pd

def ingest():
    raw_path = abs_ff_path("../data/raw/customer_purchases_large.csv")
    df = pd.read_csv(raw_path)
