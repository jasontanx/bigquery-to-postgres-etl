# bigquery-to-postgres-etl

Stage 1 (Extract - Load)
[ Source --> BQ, Destination --> Postgres]
1. Ingest data to BQ from Gsheet
2. Extract data from bigquery
3. Ingest data into Postgres DB

Stage 2 (Extract - Load)
[ Destination --> Postgre, Source --> BQ]
1. Extract data from Postgres DB via query 
2. Save queried output into dataframe
3. ingest the data into bigquery with new file name
