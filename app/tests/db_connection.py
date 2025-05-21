import psycopg2
from psycopg2 import sql
from decouple import config

#Connect to postgress using environment variables
def connect_db():
    conn = psycopg2.connect(
        dbname=config('POSTGRES_DB_NAME'),
        user=config('POSTGRES_USER'),
        password=config('POSTGRES_PASSWORD'),
        host=config('POSTGRES_HOST'),
        port=config('POSTGRES_PORT')
    )
    return conn

    
print(connect_db())