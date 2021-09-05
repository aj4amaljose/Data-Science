
def df_db_load(df, table, db_engine, chunksize, if_exists):
    df.to_sql(table,
              con=db_engine,
              chunksize=chunksize,
              if_exists=if_exists)