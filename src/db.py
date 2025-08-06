import psycopg2

def connect(db_host, db_name, db_username, db_password):
    conn_string = f'host={db_host} dbname={db_name} user={db_username} password={db_password}'
    conn = psycopg2.connect(conn_string)

    return conn