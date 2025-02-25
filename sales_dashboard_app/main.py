from fastapi import FastAPI
from app.routers import sales_dashboard_router
from database_config.connection import Base, get_engine

app = FastAPI(title="Sales Dashboard Application", version="1.0")

# Database initialization
engine = get_engine()
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(sales_dashboard_router.router, prefix="/sales", tags=["Sales"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
