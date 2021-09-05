"""
Entrypoint Module for the data pipe line application
"""
from configurations import db_connection_string
from extraction.handlers import process_zip_file
from transform.main import entry_point as transform_entry
from data_load.main import entrypoint as data_load


def entrypoint(file_path, file_type_in_zip):
    """
    Entrypoint method

    :param file_path: File path
    :param file_type_in_zip: Type of the file in the zip
    :return:
    """
    for df in process_zip_file(file_path, file_type_in_zip):
        process_df(df)

def process_df(df):
    """
    Transforms Dataframe and load the data to the database
    :param df: Dataframe
    """

    if not df.empty: # Check Dataframe is empty or not
        df = transform_entry(df) # Transforms the Dataframe

    data_load(df, connection_string=db_connection_string) # Loads data to the given db


# if __name__ == '__main__':
    # entrypoint(file_path=r"C:\Users\amalj\Downloads\test_data.zip", file_type_in_zip='newline_delimited_json')
