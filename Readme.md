## Project: Scalable Customer Purchase Analytics Platform

### Project Goal
Build a modular, memory-efficient, testable Python package that loads, cleans, aggregates, and profiles customer purchase data from a large CSV file and generates summary reports. The pipeline should be chunk-friendly, reproducible, and tested.

#### Dataset
Customer purchases dataset (~10M rows):
Each row includes:
- customer_id (int)
- purchase_id (str)
- product_category (str)
- purchase_amount (float)
- purchase_date (datetime)
- country_code (str)
- customer_age (int)
- payment_type (str)

You can also generate synthetic data using Faker to make dataset larger.

#### Project Requirements
##### Project Initialization & Packaging
Structure the project as a pip-installable Python package:
- Use pyproject.toml or setup.py
- Use virtual env + requirements.txt
- Enable reproducibility with .env or dotenv

##### Structure (flexible):
customer_analytics/
├── __init__.py
├── config.py
├── ingestion.py
├── cleaning.py
├── transformation.py
├── analysis.py
├── utils.py
tests/
notebooks/
data/
reports/

##### DataOps with Pandas:
Implement these as functions or pipeline steps:
- Load CSVs with configurable paths
- Handle missing data, invalid types, duplicates
- Filter out negative or implausible values (e.g., age < 10, amount < 0)
- Group by country/product and compute:
    - total revenue
    - average basket size
    - number of unique customers
    - Concatenate subsets or slices
- Log basic data summaries (logging)

##### NumPy Integration for Performance
- Use NumPy for numerical summaries: mean, std, percentiles
- Implement one vectorized computation using NumPy (e.g., Z-score or outlier filtering)
- Compare performance of loop vs NumPy (bonus)
  
##### Memory Optimization & Chunked Processing
- Use df.info(memory_usage="deep") and sys.getsizeof() to profile memory
- Optimize dtypes using downcasting strategies
- Implement a chunked reader:
  - Aggregate total revenue per country while streaming
  - Support batch size config
- Document memory gains with comments or README

##### Testing & Validation
- Use pytest to test core functions
- Validate schema using pandera
- Test:
  - No nulls in critical columns (e.g., purchase_amount)
  - All countries are in known ISO codes
  - No duplicate purchase_ids
  - Revenue never negative
- Use test data fixtures (you can simulate or truncate)
- Optional:
    - Add test coverage for chunked processing
    - Add property-based tests using hypothesis

##### Reporting & Drift Detection
- Generate a summary report using ydata-profiling or pandas-profiling
- Simulate drift by:
    - Injecting a rare payment type
    - Shifting average purchase amount
- Compare and log differences across runs

##### Bonus Challenges
- Add logger with timestamped logs per run
- Generate HTML report from metrics