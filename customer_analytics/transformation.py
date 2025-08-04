import pandas as pd
from customer_analytics.logger import get_logger

def transform(df_iter):
    get_logger.info("Transformation starting...")
    for chunk in df_iter:
        get_logger.info("dropping NaNs")
        chunk = chunk.dropna(subset=['customer_id', 'purchase_id', 'purchase_amount'])
        get_logger.info("handling invalid types")
        chunk['purchase_date'] = pd.to_datetime(chunk['purchase_date'], errors='coerce')
        for col in ["customer_id", "customer_age", "purchase_amount"]:
            chunk[col] = pd.to_numeric(chunk[col], errors='coerce')
        for col in ["purchase_id", "product_category", "country_code", "payment_type"]:
            chunk[col] = chunk[col].apply(lambda x: x if isinstance(x, str) else None)
        for col in ["product_category", "country_code", "payment_type"]:
            chunk[col] = chunk[col].astype('category')
        get_logger.info("dropping NaNs after invalid types")
        chunk = chunk.dropna(subset=['customer_id', 'purchase_id', 'purchase_amount'])
        get_logger.info("handling duplicates")
        chunk = chunk.drop_duplicates()
        get_logger.info("Filter out negative or implausible values (e.g., age < 10, amount < 0)")
        chunk = chunk[(chunk["customer_age"] >= 10) & (chunk["purchase_amount"] > 0)]
        #id payment type, 
        get_logger.info("Grouping by country...")
        total_revenue_c = chunk.groupby('country_code')['purchase_amount'].sum()
        purchase_count_c = chunk.groupby('country_code')['purchase_amount'].count()
        avg_bask_c = total_revenue_c / purchase_count_c
        n_unique_customers_c = chunk.groupby('country_code')['customer_id'].nunique()
        get_logger.info("Grouping by product...")
        total_revenue_p = chunk.groupby('product_category')['purchase_amount'].sum()
        purchase_count_p = chunk.groupby('product_category')['purchase_amount'].count()
        avg_bask_p = total_revenue_p / purchase_count_p
        n_unique_customers_p = chunk.groupby('product_category')['customer_id'].nunique()