
def entry_point(file_path, type='newline_delimited_json'):
    df = read_newline_delimited_json_file(path=file_path)
    return df