import csv
import os

from seleniumbase import SB
from datetime import datetime

WORKDIR = os.getcwd()   

def start(URL, WEBSITE):
    cars_dict = {
            'url' : [], 'price' : [], 'title' : [],
            'year' : [], 'mileage' : [], 'fuel_type' : [],
            'location' : [], 'creation_date' : [], 'm_scraping_datetime' : []
    }

    with SB(uc=True, headless=True) as sb:
        sb.open(URL)

        with open(f'{WORKDIR}/src/stg/{WEBSITE}_cars.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(k for k in cars_dict.keys())

            last_page_num = sb.find_elements('//div[@role="navigation"]/ul/li', by='xpath')[-2]

            for page in range(1, last_page_num):
                sb.open(f'{URL}/?page={page}')
                
                url_webelement_list = sb.find_elements('//li[@aria-label="Listing"]/article/div/div/a', by='xpath')
                cars_dict['url'] = [webelement.get_attribute('href') for webelement in url_webelement_list]

                price_webelement_list = sb.find_elements('//div[@aria-label="Price"]/span', by='xpath')
                cars_dict['price'] = [webelement.text for webelement in price_webelement_list]

                title_webelement_list = sb.find_elements('//div[@aria-label="Title"]/h2', by='xpath')
                cars_dict['title'] = [webelement.text for webelement in title_webelement_list]

                year_webelement_list = sb.find_elements('//div[@aria-label="Subtitle"]/div/span[@aria-label="Year"]/span', by='xpath')
                cars_dict['year'] = [webelement.text for webelement in year_webelement_list]

                mileage_webelement_list = sb.find_elements('//div[@aria-label="Subtitle"]/div/span[@aria-label="Mileage"]/span', by='xpath')
                cars_dict['mileage'] = [webelement.text for webelement in mileage_webelement_list]

                fuel_type_webelement_list = sb.find_elements('//div[@aria-label="Subtitle"]/div/span[@aria-label="FuelType"]/span', by='xpath')
                cars_dict['fuel_type'] = [webelement.text for webelement in fuel_type_webelement_list]

                location_webelement_list = sb.find_elements('//div/div/div/span[@aria-label="Location"]', by='xpath')
                cars_dict['location'] = [webelement.text for webelement in location_webelement_list]

                creation_date_webelement_list = sb.find_elements('//div/div/div/span/span[@aria-label="Creation date"]', by='xpath')
                cars_dict['creation_date'] = [webelement.text for webelement in creation_date_webelement_list]

                cars_dict['m_scraping_datetime'] = [datetime.now().strftime('%Y-%m-%d %H-%M-00') for _ in range(len(cars_dict['creation_date']))]

                tmp_list = [v for v in cars_dict.values()]
                transposed_list = list(zip(*tmp_list))
                writer.writerows(transposed_list)

                


        # {prices : [
        #               [page_1_price, page_1_price, page_1_price],
        #               [page_2_price, page_2_price, page_2_price],
        #               [page_3_price, page_3_price, page_3_price],
        #           ]
        # }