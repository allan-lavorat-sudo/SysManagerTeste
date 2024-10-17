import pandas as pd
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from datetime import datetime

def ingest_data():
    # Conecte ao PostgreSQL
    engine = sqlalchemy.create_engine('postgresql+psycopg2://airflow:airflow@postgres/airflow')
    
    # Leia o arquivo CSV
    df = pd.read_csv('/usr/local/airflow/data/sales_data_example 1.csv')  # Certifique-se de que esse é o caminho correto
    
    # Carregue os dados para a tabela raw_data
    df.to_sql('raw_data', engine, if_exists='replace', index=False)

def transform_data():
    df = pd.read_csv('/path/to/local/dir/my_sales_data.csv')
    total_revenue_per_customer = df.groupby('customer_id')['price'].sum()
    sales_per_product = df.groupby('product_id')['quantity'].sum()
    total_revenue_per_month = df.groupby(df['order_date'].dt.to_period('M'))['price'].sum()

    total_revenue_per_customer.to_csv('/path/to/local/dir/total_revenue_per_customer.csv', index=False)
    sales_per_product.to_csv('/path/to/local/dir/sales_per_product.csv', index=False)
    total_revenue_per_month.to_csv('/path/to/local/dir/total_revenue_per_month.csv', index=False)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
}

with DAG('data_pipeline', default_args=default_args, schedule_interval='@daily') as dag:
    ingest_task = PythonOperator(
        task_id='ingest_data',
        python_callable=ingest_data
    )
    
    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data
    )

    ingest_task >> transform_task
