from data_pipline_app.data_pipline_app.configurations import db_connection_string
from extraction.handlers import process_zip_file
from transform.main import entry_point as transform_entry
from data_load.main import entrypoint as data_load


def entrypoint(file_path, file_type_in_zip):
    for df in process_zip_file(file_path, file_type_in_zip):
        process_df(df)

def process_df(df):
    if not df.empty:
        df = transform_entry(df)
    data_load(df, connection_string=db_connection_string)


if __name__ == '__main__':
    entrypoint(file_path=r"C:\Users\amalj\Downloads\test_data.zip", file_type_in_zip='newline_delimited_json')
