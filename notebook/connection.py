import os
import psycopg2
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type


# TODO: retry is required until db is ready for connection.
#  consider using health check in compose.yml which might be neater.
@retry(stop=stop_after_attempt(5),
       wait=wait_exponential(multiplier=1, min=3, max=10), reraise=True,
       retry=retry_if_exception_type(psycopg2.OperationalError))
def connect_to_db():
    """
    Connects to PostgreSQL and returns the connection instance.
    :return: Connection instance
    """
    try:
        connection = psycopg2.connect(
            host=os.environ["POSTGRES_HOST"],
            database=os.environ["POSTGRES_DB"],
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"]
        )
        return connection
    except psycopg2.OperationalError as e:
        print(f'Failed to connect to DB with error {e}. Retry...')
        raise
