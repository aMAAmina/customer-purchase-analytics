import argparse
from customer_analytics.pipeline import run_pipeline 

def main():
    parser = argparse.ArgumentParser(description="Run the customer purchase pipeline.")
    parser.add_argument("--datapath", help="configure the path to processed CSV data")
    args = parser.parse_args()

    run_pipeline(datapath=str(args.datapath) if args.datapath else None)

if __name__ == "__main__":
    main()