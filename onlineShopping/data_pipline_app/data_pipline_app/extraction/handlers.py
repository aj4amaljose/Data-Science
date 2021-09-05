"""
Handles extraction for different file types
"""
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
    """
    Read newline delimited json

    :param io_file: Io file reference
    :return: Dataframe
    """
    try:
        data_frame = pd.read_json(io_file, lines=True)
        return data_frame
    except Exception as e:
        print(e)


def read_yaml(file_path):
    """
    Read yaml file

    :param file_path: File path
    :return: Yaml data
    """
    config = dict()
    with open(file_path, 'r') as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
        finally:
            return config


def process_zip_file(file_path, file_type_in_zip):
    """
    Process zip file

    :param file_path: File path
    :param file_type_in_zip: File type in zip file
    :return:
    """
    try:
        zip_file_handler = zipfile.ZipFile(file_path, 'r')
        password=hashlib.sha256(file_extraction_password.encode('ascii')).hexdigest()
        for _file in zip_file_handler.namelist():
            yield handler_mapping[file_type_in_zip](io_file=zip_file_handler.open(_file, pwd=bytes(password, 'utf-8')))
    except Exception as exc:
        print(exc)
