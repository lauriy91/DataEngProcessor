# ETL - Sales Dashboard App

The goal of this project is to build a simple sales dashboard application. The application will ingest and process sales data, clean and transform it, store it efficiently, and provide a RESTful API to serve the processed data.

## Technical Specifications
- Programming Language: Python
- Database: SQLite
- Libraries:
  - pandas and porlas for data manipulation
  - sqlalchemy for database interactions
  - fastapi for API development
- uvicorn for running FastAPI
- Necessaries modules and libreries for **Sales Dashboard App** (in [requirements.txt](./requirements.txt)).

## Modules
- data ([`modulos.data`](./modulos/data)): csv records
- utils ([`modulos.utils`](./modulos/utils)): tools for easy development
- extract ([`modulos.extract`](./modulos/extract)): extract data from csv
- transform ([`modulos.transform`](./modulos/transform)): transform data from csv
- load ([`modulos.load`](./modulos/load)): load data from csv files into database
- database ([`modulos.database`](./modulos/database)): database configuration

## Project Initialization
- Clone the repository:
  git clone <repository_url>
  cd sales-dashboard 
- Create a virtual environment
  python -m venv venv
  source venv/bin/activate
- Install dependencies
  pip install -r requirements.txt

## Tools
- Python
- Pandas
- SQLAlchemy
- SQLite

## Endpoints

- GET /sales/product
- GET /sales/day
- GET /sales/category
- GET /sales/outliers

## Deliverables

A Python script for data processing.
A RESTful API built with FastAPI.