from sqlalchemy import create_engine
from data_pipline_app.configurations import db_connection_string
engine = create_engine(db_connection_string)
def entrypoint(df):
    df.to_sql('Customers',
              con=engine,
              chunksize=1000,
              if_exists="replace")