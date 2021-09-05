"""
Handles database engine
"""
from contextlib import contextmanager
from sqlalchemy import create_engine

def create_engine_local(db_connection_string):
    """
    Create Engine using the connection string

    :param db_connection_string: Connection string
    :return: Engine
    """
    return create_engine(db_connection_string)


@contextmanager
def engine_scope(engine):
    """
    Manages Engine during function execution
    """
    try:
        yield
    except:
        engine.dispose()
    finally:
        engine.dispose()
