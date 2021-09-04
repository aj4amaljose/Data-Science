import os

file_extraction_password = os.environ.get("file_extraction_password")
file_destination = os.environ.get("file_destination")
db_connection_string = os.environ.get(
    "connection_string") or r"sqlite:///C:\Users\amalj\PycharmProjects\onlineShopping.db"
