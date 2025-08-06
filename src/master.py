import dotenv
import os
import json

import db


# GLOBAL SETTINGS
# =======
PWD = os.getcwd()

dotenv.load_dotenv(f'{PWD}/db.env')
DB_HOST     = os.getenv('POSTGRES_HOST')
DB_NAME     = os.getenv('POSTGRES_DB')
DB_USER     = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')


# Initiates a connection to the database
conn = db.connect(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD)

# Closes the connection to the database
conn.close()