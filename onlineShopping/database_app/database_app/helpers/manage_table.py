"""
Module to create or delete the table
"""

from models import customers
from connection import connection_string

engine_model_mappings = {
    'customers': [connection_string, customers]
}


def manage_all_tables(action, db_engine, db_model):
    """
    Deletes or Creates db if not created

    :param action: action to be performed
    :param db_engine: DB engine
    :param db_model: DB schema model
    """

    base = db_model.Base
    if action == 'create':
        base.metadata.create_all(bind=db_engine)
    else:
        base.metadata.drop_all(bind=db_engine)
