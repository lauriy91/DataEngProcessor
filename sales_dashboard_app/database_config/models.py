from sqlalchemy import Column, Integer, String, Float, Boolean, Date
from database_config.connection import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    category = Column(String, nullable=False)
    product = Column(String, nullable=False)
    quantity = Column(Integer, default=0)
    price = Column(Float, nullable=False)
    total_sales = Column(Float)
    day_of_week = Column(String)
    high_volume = Column(Boolean, default=False)

class AggregatedMetricsByCategory(Base):
    __tablename__ = "aggregated_metrics"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, nullable=False)
    avg_price = Column(Float)
    total_revenue = Column(Float)
    best_sales_day = Column(String)

class Outlier(Base):
    __tablename__ = "outliers"

    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    outlier_flag = Column(Boolean, default=True)
