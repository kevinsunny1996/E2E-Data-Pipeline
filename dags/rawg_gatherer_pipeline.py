# Airflow modules import
from datetime import timedelta
from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

# Custom modules import
from .utils.logger import LoggerFactory
from .utils.rawg_caller import RAWGAPIResultFetcher
from .utils.secret_retriever import CloudUtils
from .utils.url_generator import generate_full_url

# Default DAG arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    # 'email': ['<EMAIL>'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

# DAG definition
@dag(
    dag_id='rawg_data_extraction_and_load_to_GCS',
    default_args=default_args,
    description='DAG to fetch RAWG API data and load it in GCS',
    schedule=None,
    start_date=days_ago(2),
    tags=['rawg_api_elt'],
    catchup=False
)
def data_fetcher_dag():
    @task
    def get_rawg_api_key() -> str:
        """
            Gets API Key stored in GCP Secrets Manager for RAWG account

            Returns:
                RAWG API Key as a string.
        """
        return CloudUtils.get_secret('RAWG_API_KEY')

    @task
    def get_spotify_ids() -> list:
        pass

    @task
    def get_related_spotify_data() -> dict:
        pass

    # store_spotify_output_to_bucket = GCS