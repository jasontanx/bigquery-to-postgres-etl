'''
author: jason
creation date: 26/3/2023

main.py --> extract.py
'''

import argparse
import json
from datetime import datetime, timedelta
# import os
# import paramiko
from extract import extract_data_from_query
from ingest import ingest

from sqlalchemy import create_engine


def main(params) -> None:
    user = params.user
    password = params.password
    host = params.host 
    port = params.port 
    db = params.db
    table_name = params.table_name

    date_fmt = datetime.now().strftime("%Y%m%d") + ".csv"
    file_name = "social_demo_2021_data" + date_fmt

    extract_data_from_query(file_name) #args.project_id, args.query, args.output_path

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    engine.connect()
    print('engine.connect')
    ingest(file_name, table_name, engine)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')
    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--table_name', required=True, help='name of the table where we will write the results to')
    args = parser.parse_args()
    main(args)
