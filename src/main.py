import mysql.connector
from etl.extract import extract
from etl.transform import transform
from etl.load import load

def run_etl(file_path: str, database):
    data = extract(file_path)
    transformed_data = transform(data)
    transformed_data.to_csv("data/processed/jobs_cleaned.csv")
    load(transformed_data, database)

if __name__ == "__main__":
    # conn = mysql.connector.connect(
    #     host="localhost",
    #     user="root",
    #     password="Bi08112002#",
    #     database="job_db"
    # )

    # cursor = conn.cursor()
    # cursor.execute("Drop table job_db.jobs")

    run_etl(
        file_path="data/raw/jobs.csv",
        database="job_db"
    )