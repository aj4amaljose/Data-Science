from data_pipline_app.transform.transforms import *


def entry_point(df):
    df = df.drop(columns=set({column for column in df.columns} - set(column_schema.keys())))

    df_cleansing(df=df,
                 df_schema=df_schema,
                 sequence="initial_cleansing",
                 kwargs=dict())

    column_cleansing_method_info = group_column_cleansing_methods(schema=column_schema)
    column_cleansing_execution(column_cleansing_method_info, df)
    df_cleansing(df=df,
                 df_schema=df_schema,
                 sequence="post_column_cleansing",
                 kwargs=dict(column_schema=column_schema))
    return df