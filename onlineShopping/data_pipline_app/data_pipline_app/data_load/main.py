from data_load.rdbms.ingest import main
from data_load.rdbms.ingest.engine_handler import create_engine_local, engine_scope


def entrypoint(df, connection_string, database_type='rdbms'):
    if database_type == 'rdbms':
        engine = create_engine_local(connection_string)
        with engine_scope(engine):
            main.df_db_load(df=df, table='Customers', db_engine=engine, chunksize=1000, if_exists="replace")