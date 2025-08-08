import dotenv
import os
import db
import docker


# GLOBAL SETTINGS
# =======
PWD = os.getcwd()

dotenv.load_dotenv(f'{PWD}/db.env')
DB_HOST     = os.getenv('POSTGRES_HOST')
DB_NAME     = os.getenv('POSTGRES_DB')
DB_USER     = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')


# Instantiates a connection to the database
conn = db.connect(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD)

# Get list of websites to be scraped
with conn:
    with conn.cursor() as curs:
        curs.execute(
            'SELECT * FROM website_config'
        )
        website_list = curs.fetchall()

# Scraper containers will be instantiated 
# based on the number of websites fetched
# using the docker python API

# RETURN VAL:
# [
#     (id, name, url),
#     (id, name, url),
#     ...
# ]

# FIXME: nesting should not start from the
# website for loop as the other containers will
# be waiting
for website in website_list:
    category_list = db.fetch_config(conn, 'category_config', 'website', website)

for category in category_list:
    subcategory_list = db.fetch_config(conn, 'subcategory_config', 'category', category)

    for subcategory in subcategory_list:
        element_list = db.fetch_config(conn, 'element_config', 'subcategory', subcategory)

        for element in element_list:
            pass
                


# Closes the connection to the database
conn.close()