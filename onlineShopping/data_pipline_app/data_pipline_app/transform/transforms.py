import os
from collections import defaultdict
from .handlers import handler_mapping, df_schema, column_schema


def group_column_cleansing_methods(schema):
    column_cleansing_method_info = defaultdict(dict)

    for details in schema.items():
        column, column_detail = details
        cleansing_methods = column_detail.get('cleansing_methods', [])
        create_cleansing_sequence(column, cleansing_methods, column_cleansing_method_info)
    return column_cleansing_method_info


def create_cleansing_sequence(column, cleansing_methods, method_info):
    for index, method in enumerate(cleansing_methods):
        if method in method_info[index]:
            method_info[index][method].append(column)
        else:
            method_info[index][method] = [column]


def column_cleansing_execution(column_cleansing_info, df):
    sequences = sorted(column_cleansing_info.keys())
    for sequence in sequences:
        for method_details in column_cleansing_info[sequence].items():
            method, columns = method_details
            handler_mapping[method](df, columns)


def df_cleansing(df, df_schema, sequence, kwargs):
    args = [df, kwargs] if kwargs else [df]

    for method in df_schema[sequence]:
        handler_mapping[method](*args)
