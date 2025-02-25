from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from database_config.connection import Base

class Transactions(Base):
    __tablename__ = "transactions"

    transaction_id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, index=True)
    category = Column(String, index=True)
    product = Column(String, index=True)
    quantity = Column(Integer)
    price = Column(Float)
    total_sales = Column(Float)
    day_of_week = Column(String)
    high_volume = Column(Boolean)
    average_price = Column(Float)
    total_revenue = Column(Float)
    day_with_highest_sales = Column(String)
    mean_quantity = Column(Float)
    outliers_std_deviations = Column(Float)
    outlier_flag = Column(Boolean)

class Outliers(Base):
    __tablename__ = "outliers"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)
    quantity = Column(Integer)
    mean_quantity = Column(Float)
    outliers_std_deviations = Column(Float)
    outlier_flag = Column(Boolean)

class CategoryMetrics(Base):
    __tablename__ = "category_metrics"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)
    average_price = Column(Float)
    total_revenue = Column(Float)
    day_with_highest_sales = Column(String)