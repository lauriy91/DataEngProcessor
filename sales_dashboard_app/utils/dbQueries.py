# sales_dashboard_app/utils/db_queries.py
def get_total_sales_by_product(cursor, product_name=None, category=None):
    query = """
    SELECT product_name, category, SUM(total_sales) AS total_sales
    FROM transactions
    WHERE 1=1
    """
    params = []
    if product_name:
        query += " AND product_name = ?"
        params.append(product_name)
    if category:
        query += " AND category = ?"
        params.append(category)
    query += " GROUP BY product_name, category"
    
    cursor.execute(query, params)
    return cursor.fetchall()

def get_all_sales_by_day(cursor, start_date=None, end_date=None):
    query = """
    SELECT date, SUM(total_sales) AS total_sales
    FROM transactions
    WHERE 1=1
    """
    params = []
    if start_date:
        query += " AND date >= ?"
        params.append(start_date)
    if end_date:
        query += " AND date <= ?"
        params.append(end_date)
    query += " GROUP BY date"
    
    cursor.execute(query, params)
    return cursor.fetchall()

def get_all_category_metrics(cursor):
    query = """
    SELECT category, AVG(price) AS avg_price, SUM(total_sales) AS total_revenue, day_with_highest_sales
    FROM category_metrics
    GROUP BY category
    """
    cursor.execute(query)
    return cursor.fetchall()

def get_all_outliers(cursor):
    query = "SELECT * FROM outliers"
    cursor.execute(query)
    return cursor.fetchall()
