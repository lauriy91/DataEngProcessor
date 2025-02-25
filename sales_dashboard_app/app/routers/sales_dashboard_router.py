from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from database_config.connection import get_db
from app.services.sales_dashboard_service import SalesDashboardService

router = APIRouter()
sales_service = SalesDashboardService()


@router.get("/product")
def get_sales_by_product(
    product: str = Query(None, description="Product Name"),
    category: str = Query(None, description="Product Category"),
    db: Session = Depends(get_db),
):
    return SalesDashboardService.get_sales_by_product_service(db, product, category)
