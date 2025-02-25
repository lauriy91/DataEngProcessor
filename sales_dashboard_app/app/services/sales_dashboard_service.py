from sqlalchemy.orm import Session
from sqlalchemy import func
from database_config.models import Transactions

class SalesDashboardService:
    @staticmethod
    def get_sales_by_product_service(db: Session, product: str = None, category: str = None):
        query = db.query(
            Transactions.product,
            func.sum(Transactions.total_sales).label("total_sales"),
            func.sum(Transactions.total_revenue).label("total_revenue"),
            func.avg(Transactions.average_price).label("average_price")
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
                "average_price": row[3]
            }
            for row in results
        ]