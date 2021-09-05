import argparse
from sqlalchemy import create_engine
from helpers.manage_table import engine_model_mappings, manage_all_tables

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='manage app tables')
    choices = ['create', 'delete']
    parser.add_argument('-a', '--action', dest='action', choices=choices,
                        help='Manges tables required for the app, choices are create or action',
                        required=True)
    args = parser.parse_args()
    for schema in engine_model_mappings.keys():
        db_url = engine_model_mappings[schema][0]
        model = engine_model_mappings[schema][1]
        engine = create_engine(db_url)
        manage_all_tables(action=args.action, db_engine=engine, db_model=model)
        engine.dispose()