import pandas as pd
from time import time


def ingest(csv_file, table_name, engine, chunksize=100000):
    '''
    ingest queried data into postgres
    
    '''
    df_iter = pd.read_csv(csv_file, iterator=True, chunksize=chunksize)
    run = True
    while run:
        try:
            t_start = time()
            df = next(df_iter)
            df.to_sql(name=table_name, con=engine, if_exists='append')
            t_end = time()
            print(f'inserted another chunk, took {t_end-t_start:.3f} seconds')
        except Exception:
            run = False
