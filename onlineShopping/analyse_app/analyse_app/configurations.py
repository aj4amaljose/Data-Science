import os

app_host = os.environ.get("app_host") or 'localhost'
app_port = os.environ.get("app_port") or 8000
db_connection_string = os.environ.get(
    "connection_string")
