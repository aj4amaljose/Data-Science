import os
import pandas as pd
import numpy as np
from collections import defaultdict
from common.helpers import mapping, set_handler_mapping
from extraction.handlers import read_yaml

df_schema = read_yaml(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   '../schema/df_schema.yaml'))
column_schema = read_yaml(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                       '../schema/column_schema.yaml'))
handler_mapping = mapping


def drop_rows_with_values_less_than_zero(df, cols):
    df[cols] = df[df[cols] > 0][cols]
    df.dropna()


def find_final_datatype(data_type):
    final_datatype = None
    if data_type == 'string':
        final_datatype = str
    elif data_type == 'integer':
        final_datatype = int
    elif data_type == 'float':
        final_datatype = float
    return final_datatype


def replace_values_in_column(df, columns, current_value, new_value):
    df[columns] = df[columns].replace(current_value, new_value)


def remove_duplicates_and_keep_one(df, columns, keep):
    df = df.drop_duplicates(subset=columns, keep=keep)


def replace_string_with_integer_float_columns(df, columns, value):
    df[columns] = df[columns].apply(lambda x: pd.to_numeric(x, errors='coerce')).fillna(value)


def replace_all_negative_values(df, value):
    new_df = df._get_numeric_data()
    new_df[new_df < 0] = value


@set_handler_mapping(operation="convert_datatype")
def convert_final_datatype(df, kwargs):
    column_schema = kwargs['column_schema']
    column_data_types = defaultdict(list)

    for column_info in column_schema.items():
        column, _column_info = column_info
        column_data_types[_column_info['type']].append(column)

    for data_type in column_data_types.keys():
        final_datatype = find_final_datatype(data_type)
        convert_columns_to_final_datatype(df, column_data_types[data_type], final_datatype)


def convert_columns_to_final_datatype(df, columns, final_datatype):
    if final_datatype:
        df[columns] = df[columns].astype(final_datatype)


@set_handler_mapping(operation='string_to_zero')
def string_to_zero(df, columns):
    replace_string_with_integer_float_columns(df, columns, 0)

@set_handler_mapping(operation='nan_to_zero')
def nan_to_zero(df, columns):
    replace_values_in_column(df, columns, np.nan, 0)

@set_handler_mapping(operation="replace_unallowed_values")
def replace_unallowed_values(df, columns):
    for column in columns:
        allowed_values = column_schema[column].get("allowed_values", None)
        default_value = column_schema[column].get("default_value", None)
        if allowed_values:
            df[column] = df[column].map(lambda x: x if x in allowed_values else default_value)

@set_handler_mapping(operation='negative_to_zero')
def negative_to_zero(df, kwargs=None):
    replace_all_negative_values(df, 0)

@set_handler_mapping(operation="keep_unique_customer_ids")
def keep_unique_customer_id_rows(df):
    remove_duplicates_and_keep_one(df, columns=["customer_id"], keep="last")
