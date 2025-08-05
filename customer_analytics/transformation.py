
import pandas as pd
from customer_analytics.logger import get_logger

logger = get_logger()

def transform(df_iter):
    logger.info("Transformation starting...")
    for chunk in df_iter:
        logger.info("dropping NaNs")
        chunk = chunk.dropna(subset=['customer_id', 'purchase_id', 'purchase_amount'])
        logger.info("handling invalid types")
        chunk.loc[:, 'purchase_date'] = pd.to_datetime(chunk['purchase_date'], errors='coerce')
        for col in ["customer_id", "customer_age", "purchase_amount"]:
            chunk.loc[:, col] = pd.to_numeric(chunk[col], errors='coerce')
        for col in ["purchase_id", "product_category", "country_code", "payment_type"]:
            chunk.loc[:, col] = chunk[col].apply(lambda x: x if isinstance(x, str) else None)
        for col in ["product_category", "country_code", "payment_type"]:
            chunk.loc[:, col] = chunk[col].astype('category')
        logger.info("dropping NaNs after invalid types")
        chunk = chunk.dropna(subset=['customer_id', 'purchase_id', 'purchase_amount'])
        logger.info("handling duplicates")
        chunk = chunk.drop_duplicates()
        logger.info("Filter out negative or implausible values (e.g., age < 10, amount < 0)")
        chunk = chunk[(chunk["customer_age"] >= 10) & (chunk["purchase_amount"] > 0)]
        #id payment type, 
        logger.info("Grouping by country...")
        total_revenue_c = chunk.groupby('country_code')['purchase_amount'].sum()
        purchase_count_c = chunk.groupby('country_code')['purchase_amount'].count()
        avg_bask_c = total_revenue_c / purchase_count_c
        n_unique_customers_c = chunk.groupby('country_code')['customer_id'].nunique()
        report_lines = [
            "Gouped by country:...",
            f"total revenue = {total_revenue_c}",
            f"purchased amount = {purchase_count_c}",
            f"average of basket = {avg_bask_c}",
            f"number of unique customers = {n_unique_customers_c}",
        ]
        logger.info("Grouping by product...")
        total_revenue_p = chunk.groupby('product_category')['purchase_amount'].sum()
        purchase_count_p = chunk.groupby('product_category')['purchase_amount'].count()
        avg_bask_p = total_revenue_p / purchase_count_p
        n_unique_customers_p = chunk.groupby('product_category')['customer_id'].nunique()
        report_lines.extend([
            "Gouped by product:...",
            f"total revenue = {total_revenue_p}",
            f"purchased amount = {purchase_count_p}",
            f"average of basket = {avg_bask_p}",
            f"number of unique customers = {n_unique_customers_p}",
        ])
        for line in report_lines:
            print(line)