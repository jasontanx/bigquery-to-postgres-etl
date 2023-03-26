import time
import logging
from google.cloud import bigquery
# from sql import query

# import pandas as pd
# from pandas import DataFrame
# from datetime import datetime


def get_logging_format() -> logging.Logger:
    """
    function to return custom format logging

    return logging.Logger
    """

    logging.Formatter.converter = time.gmtime
    logging.basicConfig(
        format="[%(asctime)s,%(msecs)d] %(levelname)-8s [%(filename)s:%(lineno)d] - %(message)s",
        datefmt="%Y-%m-%d, %H:%M:%S",
        level=logging.INFO,
    )
    _logger: logging.Logger = logging.getLogger("de-logging")
    return _logger


logger: logging.Logger = get_logging_format()


def extract_data_from_query(file_name): #file_name, query_loc: str
    """
    Extract Data from Bigquery table with prepared query
    """
    # final_path = temp_path + f"/{file_name}"
    bqclient = bigquery.Client.from_service_account_json('/Users/junshengtan/Desktop/personal_repo/github-to-bq/secret_key.json')
    
    job_config = bigquery.QueryJobConfig(allow_large_results=True)

    query_loc = './sql/query.sql'
    sql_file = open(query_loc, 'r')
    query_string = sql_file.read()

    sql_file.close()

    # make api request to run query
    query_job = bqclient.query(query_string, job_config=job_config)

    # wait for job to complete
    query_job.result()

    dataframe = bqclient.query(query_string).to_dataframe(create_bqstorage_client=True)
    print(dataframe.head())

    dataframe.to_csv(file_name) # output path and file_name

    logger.info("export to csv: %s", file_name)
    logger.info("Number of rows exported: %d", len(dataframe))
    logger.info(len(dataframe))

    return file_name
