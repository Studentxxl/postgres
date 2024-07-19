import psycopg2
from datetime import datetime


def time_now():
    '''  '''
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    return str(date)


def connect_db(dbname, user, password, host):
    '''  '''
    # *
    con = None
    try:
        # *
        con = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
        # *
        mess = f"Connection to {dbname} successful at {time_now()}"
        # *
        print(mess)
    # *
    except psycopg2.OperationalError as e:
        print(f"The error '{e}' occurred")
    # *
    return con





