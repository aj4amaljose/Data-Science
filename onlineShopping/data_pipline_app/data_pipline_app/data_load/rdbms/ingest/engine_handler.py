from contextlib import contextmanager
from sqlalchemy import create_engine

def create_engine_local(db_connection_string):
    return create_engine(db_connection_string)


@contextmanager
def engine_scope(engine):
    """
    Manages session during function execution
    """
    try:
        yield
    except:
        engine.dispose()
    finally:
        engine.dispose()
