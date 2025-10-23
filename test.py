import psycopg2
import csv

conn = psycopg2.connect(
    dbname="opco_db",
    user="adminuser",
    password="<your_password>",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def load_csv_to_table(csv_file, table_name, columns):
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            placeholders = ', '.join(['%s'] * len(columns))
            sql = f"INSERT INTO public.{table_name} ({', '.join(columns)}) VALUES ({placeholders}) ON CONFLICT DO NOTHING;"
            cur.execute(sql, [row[c] for c in columns])
    conn.commit()

# Load platform data
load_csv_to_table('platform.csv', 'platform_catalog', ['platform_code', 'platform_name'])

# Load practice data
load_csv_to_table('practice.csv', 'practice_catalog', ['platform_code', 'practice_code', 'practice_name'])

# Load offering data
load_csv_to_table('offering.csv', 'offering_catalog', ['platform_code', 'practice_code', 'offering_code', 'offering_name'])

cur.close()
conn.close()

print("✅ All CSV data loaded successfully!")











