from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
import sqlalchemy

def ingest_data():
    engine = sqlalchemy.create_engine('postgresql+psycopg2://airflow:airflow@postgres/airflow')
    df = pd.read_csv('C:\airflow\data\sales_data_example 1')
    df.to_sql('raw_data', engine, if_exists='replace', index=False)

def transform_data():
    engine = sqlalchemy.create_engine('postgresql+psycopg2://airflow:airflow@postgres/airflow')
    df = pd.read_sql('SELECT * FROM raw_data', engine)
    total_revenue_per_customer = df.groupby('customer_id').agg({'price': 'sum'}).reset_index()
    total_revenue_per_customer.to_sql('total_revenue_per_customer', engine, if_exists='replace', index=False)
    sales_per_product = df.groupby('product_id').agg({'quantity': 'sum'}).reset_index()
    sales_per_product.to_sql('sales_per_product', engine, if_exists='replace', index=False)
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.to_period('M')
    total_revenue_per_month = df.groupby('month').agg({'price': 'sum'}).reset_index()
    total_revenue_per_month.to_sql('total_revenue_per_month', engine, if_exists='replace', index=False)

with DAG('data_pipeline', start_date=datetime(2024, 1, 1), schedule_interval='@daily') as dag:
    ingest_task = PythonOperator(
        task_id='ingest_data',
        python_callable=ingest_data
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data
    )

    ingest_task >> transform_task
