import mysql.connector
from etl.extract import extract
from etl.transform import transform
from etl.load import load
import time

def run_etl(file_path: str, database):
    data = extract(file_path)
    transformed_data = transform(data)
    transformed_data.to_csv("data/processed/jobs_cleaned.csv")
    load(transformed_data, database)

if __name__ == "__main__":
    while (True):
        run_etl(
            file_path="data/raw/jobs.csv",
            database="job_db"
        )
        time.sleep(86400) # Run automatically every 1 day