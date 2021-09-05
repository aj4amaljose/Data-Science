import yaml
import io
import pandas as pd
import zipfile
import hashlib
from configurations import file_extraction_password
from common.helpers import mapping, set_handler_mapping

handler_mapping = mapping


@set_handler_mapping('newline_delimited_json')
def read_newline_delimited_json_file(io_file):
    try:
        data_frame = pd.read_json(io_file, lines=True)
        return data_frame
    except Exception as e:
        print(e)


def read_yaml(file_path):
    config = dict()
    with open(file_path, 'r') as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
        finally:
            return config


def process_zip_file(file_path, file_type_in_zip):
    zip_file_handler = zipfile.ZipFile(file_path, 'r')
    password=hashlib.sha256(file_extraction_password.encode('ascii')).hexdigest()
    for _file in zip_file_handler.namelist():
        yield handler_mapping[file_type_in_zip](io_file=zip_file_handler.open(_file, pwd=bytes(password, 'utf-8')))
