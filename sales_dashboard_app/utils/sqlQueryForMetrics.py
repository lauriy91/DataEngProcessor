from pathlib import Path
import sqlite3

def get_db_queries_metrics(cursor):
    query = """
    SELECT category, 
           AVG(price) AS avg_price, 
           SUM(total_sales) AS total_revenue 
    FROM transactions 
    GROUP BY category
    """
    cursor.execute(query)
    return cursor.fetchall()

# Roots
DATA_DIR = Path("sales_dashboard_app/data")
DB_FILE = DATA_DIR / "sales_dashboard_data.db"

# Connection to the database sqlite 3
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Run query
results = get_db_queries_metrics(cursor)
for i in results:
    print(i)

# Close the connection
conn.close()