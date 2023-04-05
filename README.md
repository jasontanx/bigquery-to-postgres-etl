# bigquery-to-postgres-etl

ETL --> (Extract - Load)

[ Source --> BigQuery, Destination --> Postgres]

![image](https://user-images.githubusercontent.com/116934441/227949498-df847c06-6865-40bc-b434-59996e28de93.png)

# Project Overview
**Description**: Personal project (BQ to Postgres data ingestion)

**Source**: GCP Big Query

**Apache Airflow (Orchestration Tool)** : Not Involved in this project*

**Destination**: Postgresql

**Language**: python 


**Main Tools Involved:**
1. Python (*IDE - Visual Studio Code*)
2. Google Cloud Platform account (*For extracting data from BigQuery*)
3. Docker (*Preferred*)


**Workflow**
1. Extract data from BigQuery via query
2. Save queried output into dataframe and output data as csv format
3. Ingest data into Postgres DB with new file name

**Final Outcome**

![image](https://user-images.githubusercontent.com/116934441/229813264-e66a18ec-b191-44b3-b3f0-ff384a73ce70.png)

**Extra Information**

1. Docker Compose tutorial (to run postgresql)

--> [DE Zoomcamp 1.2.5 - Running Postgres and pgAdmin with Docker-Compose](https://www.youtube.com/watch?v=hKI6PkPhpa0&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=9)


