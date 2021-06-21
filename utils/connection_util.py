from psycopg2 import connect
from psycopg2._psycopg import OperationalError
import os


def create_connection():
    try:
        conn = connect(
            host=('goettedb.cknyvmw7amuc.us-east-2.rds.amazonaws.com'),  # os.environ.get('HOST'),
            database=('postgres'),  # os.environ.get('DB'),
            user=('RobertJgoette'),  # os.environ.get('USER'),
            password=('Kita1234*'),  # os.environ.get('PW'),
            port=('5432')  # os.environ.get('PORT')
        )
        return conn
    except OperationalError as e:
        print(e)


connection = create_connection()
