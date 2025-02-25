# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import dash_bootstrap_components as dbc
# import pandas as pd
# import requests

# #  Url where de project are located
# API_URL = "http://127.0.0.1:8000"

# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# def sales_dashboard_data():
#     response = requests.get(f"{API_URL}/sales/day")
#     if response.status_code == 200:
#         return pd.DataFrame(response.json())
#     return pd.DataFrame()

# app.layout = dbc.Container([
#     html.H1("Sales Dashboard"),
    
#     html.Label("filter by date:"),
#     dcc.DatePickerRange(
#         id="date_picker",
#         start_date="2024-01-01",
#         end_date="2024-12-31",
#     ),

#     dcc.Graph(id="sales_graph")
# ])

# @app.callback(
#     dash.dependencies.Output("sales_graph", "figure"),
#     [dash.dependencies.Input("date_picker", "start_date"),
#      dash.dependencies.Input("date_picker", "end_date")]
# )
# def update_graph(start_date, end_date):
#     response = requests.get(f"{API_URL}/sales/day", params={"start_date": start_date, "end_date": end_date})
#     if response.status_code == 200:
#         data = pd.DataFrame(response.json())
#         figure = {
#             "data": [{"x": data["date"], "y": data["total_sales"], "type": "line", "name": "Ventas"}],
#             "layout": {"title": "sales per day"}
#         }
#         return figure
#     return {}

# if __name__ == "__main__":
#     app.run_server(debug=True)
