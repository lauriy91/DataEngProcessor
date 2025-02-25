from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database_config.connection import SessionLocal
from database_config.models import Transaction, AggregatedMetrics, Outlier

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/sales/product")
def get_all_product_sales(db: Session = Depends(get_db)):
    return db.query(Transaction.product, Transaction.total_sales).all()

@router.get("/sales/day")
def get_all_sales_days(db: Session = Depends(get_db)):
    return db.query(AggregatedMetrics).all()

@router.get("/sales/category")
def get_all_category_metrics(db: Session = Depends(get_db)):
    return db.query(AggregatedMetrics).all()

@router.get("/sales/outliers")
def get_all_outliers(db: Session = Depends(get_db)):
    return db.query(Outlier).all()
