import pandas as pd
import os
import asyncio
import re

from googletrans import Translator
from datetime import date, timedelta
from c_logging import info, success
from tqdm import tqdm

WORKDIR = os.getcwd()


async def translate(data):
    async with Translator() as translator: 
        translated_title_list = await translator.translate(data['title'].to_list())
        translated_title_list = [title.text for title in translated_title_list]
        data['translated_title'] = translated_title_list

# TODO: FIX THIS
# returned error for the get_governorate func
# list out of index
# def get_state(datapoint):
#     return datapoint.split(sep=',')[0]

# def get_governorate(datapoint):
#     return datapoint.split(sep=',')[1]

def extract_date(datapoint):
    time_past = datapoint.split(' ')[0] 
    if re.search('hour', datapoint): 
        return date.today()
    elif re.search('day', datapoint):
        return date.today() - timedelta(days=int(time_past))
    elif re.search('week', datapoint):
        return date.today() - timedelta(weeks=int(time_past))


def start(WEBSITE, CSV_FILE_PATH):
    data = pd.read_csv(CSV_FILE_PATH)
    info('Read CSV into Pandas DataFrame', depth=1)

    data['price'] = data['price'].replace('OMR ', '', regex=True)
    data['price'] = data['price'].replace(',', '', regex=True)
    data['price'] = data['price'].astype(float)
    info('Processed price field', depth=1)

    asyncio.run(translate(data))
    info('Translated title data', depth=1)

    data['mileage'] = data['mileage'].replace(' km', '', regex=True)
    data['mileage'] = data['mileage'].replace('new', 0, regex=True)
    data['mileage'] = data['mileage'].astype(int)
    info('Processed mileage data', depth=1)

    data['location'] = data['location'].replace('•', '', regex=True)
    # data['state'] = data['location'].apply(get_state)
    # data['governorate'] = data['location'].apply(get_governorate)
    info('Processed location data', depth=1)

    data['ad_creation_date'] = data['creation_date'].apply(extract_date)
    info('Extracted advertisment creation date', depth=1)

    data.to_csv(f'{WORKDIR}/src/final/{WEBSITE}_{date.today()}.csv')
    success('Written processed data to csv file')

start('dubizzle', f'{WORKDIR}/src/stg/dubbizle_2025-08-17.csv')
    