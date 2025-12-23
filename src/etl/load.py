import mysql.connector

def load(df, database):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Bi08112002#",
        database=database
    )
    cursor = conn.cursor(buffered=True)

    cursor.execute('''
        create table if not exists jobs(
            created_date date,
            position varchar(255),
            level varchar(255),
            company varchar(255),
            min_salary varchar(255),
            max_salary varchar(255),
            salary_unit varchar(255),
            city varchar(255),
            district varchar(500),
            time_remaining varchar(255),
            link varchar(255)
        );
    ''')

    for _, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT INTO jobs (created_date, position, level, company, min_salary, max_salary, salary_unit, city, district, time_remaining, link)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (row["created_date"],row["position"], row["level"],row["company"],row["min_salary"],row["max_salary"],row["salary_unit"], row["city"], row["district"], row["time"],row["link_description"])
            )
        except Exception as e:
            print("Error in load function:", e)
    
    conn.commit()
    conn.close()