import sqlite3

db_path = "sales_dashboard_app/data/sales_dashboard_data.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("DROP TABLE outliers_old;")
conn.commit()


cursor.execute(
    """
CREATE TABLE outliers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    quantity REAL,
    mean_quantity REAL,
    outliars_std_deviations REAL,
    outliar_flag REAL,      
);
"""
)
conn.commit()


cursor.execute(
    """
INSERT INTO outliers (category, quantity, mean_quantity, outliers_std_deviations, outlier_flag)
SELECT category, quantity, mean_quantity, outliers_std_deviations, outlier_flag FROM outliers_old;
"""
)
conn.commit()

conn.close()
