"""
Load dataframe into database
"""
def df_db_load(df, table, db_engine, chunksize, if_exists):
    """
    Loads Dataframe into database

    :param df: Dataframe
    :param table: Table
    :param db_engine: Database engine
    :param chunksize: Chunkzize of rows to be imported to the db
    :param if_exists: action if the row exists
    """
    df.to_sql(table,
              con=db_engine,
              chunksize=chunksize,
              if_exists=if_exists)