from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from datetime import date
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


@router.get("/day")
def get_total_sales_by_day(
    start_date: date = Query(None, description="Start date (YYYY-MM-DD)"),
    end_date: date = Query(None, description="End date (YYYY-MM-DD)"),
    db: Session = Depends(get_db),
):
    return SalesDashboardService.get_total_sales_by_day(db, start_date, end_date)


@router.get("/category")
def get_category_metrics_sales(db: Session = Depends(get_db)):
    return SalesDashboardService.get_category_metrics(db)


@router.get("/outliers")
def get_outliers(db: Session = Depends(get_db)):
    """Obtiene transacciones marcadas como outliers"""
    return SalesDashboardService.get_outliers(db)
