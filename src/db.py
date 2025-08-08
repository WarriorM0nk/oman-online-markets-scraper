import psycopg2

def connect(db_host, db_name, db_username, db_password):
    conn_string = f'host={db_host} dbname={db_name} user={db_username} password={db_password}'
    conn = psycopg2.connect(conn_string)

    return conn

def fetch_config(connection, child_table_name, parent_name, parent_table_name):
    with connection:
        with connection.cursor() as curs:
            curs.execute(
                f'SELECT * FROM {child_table_name}' \
                f'   WHERE {parent_name} = %s;',
            (parent_table_name[0], ))
            return curs.fetchall()