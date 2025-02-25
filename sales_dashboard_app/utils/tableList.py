import sqlite3

db_path = "sales_dashboard_app/data/sales_dashboard_data.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tablas en la base de datos:", tables)

conn.close()
