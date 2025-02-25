from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date
from database_config.models import Transactions, CategoryMetrics, Outliers
from sqlalchemy.exc import SQLAlchemyError


class SalesDashboardService:
    @staticmethod
    def get_sales_by_product_service(
        db: Session, product: str = None, category: str = None
    ):
        try:
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

            products = query.all()

            return [
                {
                    "product": product[0],
                    "total_sales": product[1],
                    "total_revenue": product[2],
                    "average_price": product[3],
                }
                for product in products
            ]
        except SQLAlchemyError as e:
            return {"error": f"Error fetching sales by product: {str(e)}"}

    @staticmethod
    def get_total_sales_by_day(
        db: Session, start_date: date = None, end_date: date = None
    ):
        try:
            query = db.query(
                Transactions.date,
                func.sum(Transactions.total_sales).label("total_sales"),
                func.sum(Transactions.total_revenue).label("total_revenue"),
            ).group_by(Transactions.date)

            if start_date:
                query = query.filter(Transactions.date >= start_date)
            if end_date:
                query = query.filter(Transactions.date <= end_date)

            products = query.all()

            return [
                {
                    "date": product[0].strftime("%Y-%m-%d"),
                    "total_sales": product[1],
                    "total_revenue": product[2],
                }
                for product in products
            ]
        except SQLAlchemyError as e:
            return {"error": f"Error fetching total sales by day: {str(e)}"}

    @staticmethod
    def get_category_metrics(db: Session):
        try:
            return db.query(CategoryMetrics).all()
        except SQLAlchemyError as e:
            return {"error": f"Error fetching category metrics: {str(e)}"}

    @staticmethod
    def get_outliers(db: Session):
        try:
            return db.query(Outliers).all()
        except SQLAlchemyError as e:
            return {"error": f"Error fetching outliers: {str(e)}"}
