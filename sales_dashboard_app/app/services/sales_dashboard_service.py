from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date
from database_config.models import Transactions, CategoryMetrics


class SalesDashboardService:
    @staticmethod
    def get_sales_by_product_service(
        db: Session, product: str = None, category: str = None
    ):
        query = db.query(
            Transactions.product,
            func.sum(Transactions.total_sales).label("total_sales"),
            func.sum(Transactions.total_revenue).label("total_revenue"),
            func.avg(Transactions.average_price).label("average_price"),
        ).group_by(Transactions.product)

        if product:
            query = query.filter(Transactions.product == product)
        if category:
            query = query.filter(Transactions.category == category)

        results = query.all()

        # Convert results to list of dictionaries
        return [
            {
                "product": row[0],
                "total_sales": row[1],
                "total_revenue": row[2],
                "average_price": row[3],
            }
            for row in results
        ]

    @staticmethod
    def get_total_sales_by_day(
        db: Session, start_date: date = None, end_date: date = None
    ):
        query = db.query(
            Transactions.date,
            func.sum(Transactions.total_sales).label("total_sales"),
            func.sum(Transactions.total_revenue).label("total_revenue"),
        ).group_by(Transactions.date)

        if start_date:
            query = query.filter(Transactions.date >= start_date)
        if end_date:
            query = query.filter(Transactions.date <= end_date)

        # return query.all()
        results = query.all()

        # Convert results to list of dictionaries
        return [
            {
                "date": row[0].strftime("%Y-%m-%d"),
                "total_sales": row[1],
                "total_revenue": row[2],
            }
            for row in results
        ]

    @staticmethod
    def get_category_metrics(db: Session):
        """Obtiene métricas de cada categoría"""
        return db.query(CategoryMetrics).all()
