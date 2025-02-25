# sales_dashboard_app/utils/db_queries.py
def get_all_sales_by_product(cursor):
    query = """
    SELECT product_name, category, SUM(total_sales) AS total_sales
    FROM transactions
    WHERE 1=1
    """ 
    cursor.execute(query)
    return cursor.fetchall()

def get_all_sales_by_day(cursor):
    query = """
    SELECT date, SUM(total_sales) AS total_sales
    FROM transactions
    WHERE 1=1
    """
    cursor.execute(query)
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
