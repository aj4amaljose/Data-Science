"""
Dataload entrypoint
"""
from data_load.rdbms.ingest import main
from data_load.rdbms.ingest.engine_handler import create_engine_local, engine_scope


def entrypoint(df, connection_string, laod_type='rdbms'):
    """
    Hanldes different types of loads like database, file transfer

    :param df: Dataframe
    :param connection_string: Connection String
    :param laod_type: Type of load
    """
    if laod_type == 'rdbms':
        engine = create_engine_local(connection_string)
        with engine_scope(engine):
            main.df_db_load(df=df, table='Customers', db_engine=engine, chunksize=1000, if_exists="replace")