import os
import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url =params.url

    if url.endswith('.csv.gz'):
        csv_name = 'output.csv.gz'
    else:
        csv_name = 'output.csv'


    #csv download
    os.system(f"wget {url} -O {csv_name}")

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df_iter = pd.read_csv(csv_name,iterator = True,chunksize=100000)

    df = next(df_iter)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.to_sql(name=table_name,con=engine,if_exists='replace')

    df.head(n=0).to_sql(name= table_name,con=engine,if_exists="append")
    c = 0
    while True:
        t_start = time()
        df = next(df_iter)

        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        df.to_sql(name= table_name,con=engine,if_exists="append")

        t_end = time()

        print('insrted another chunk..., took %.3f second' %(t_end-t_start))
        c += t_end-t_start

    print(f"it took {c/60} minutes")

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Ingest csv to postgres')
    # user , password,port,host,databse_name,table,url
    parser.add_argument('--user',help='username for postgress')
    parser.add_argument('--password',help='password for postgress')
    parser.add_argument('--host',help='host for postgress')
    parser.add_argument('--port',help='port for postgress')
    parser.add_argument('--db',help='database name for postgress')
    parser.add_argument('--table_name',help='table to write in ')
    parser.add_argument('--url',help='url of csv file')

    args = parser.parse_args()
    main(args)
