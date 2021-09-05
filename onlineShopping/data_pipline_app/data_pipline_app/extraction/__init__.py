"""
Entry Point for extraction
"""
def entry_point(file_path, type='newline_delimited_json'):
    """
    Entrypoint Method

    :param file_path: File path
    :param type: type of file in extraction app
    :return: Dataframe
    """
    df = read_newline_delimited_json_file(path=file_path)
    return df