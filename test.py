import psycopg2

try:
    conn = psycopg2.connect(
        host="u23jghvfsddp127.postgres.database.azure.com",
        dbname="opco_db",
        user="adminuser@u23jghvfsddp127",
        password="3Jt*y38++{#mF5mpxEuf*6kMW->",
        port="5432",
        sslmode="require"
    )

    print("✅ Connected successfully!")   # inside try
    conn.close()                          # close connection

except Exception as e:
    print("❌ Connection failed:", e)














