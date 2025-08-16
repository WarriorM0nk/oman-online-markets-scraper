import scraper
import preprocessor
import glob
import os

# prettify logging
from c_logging import info, success

from multiprocessing import Process

WORKDIR = os.getcwd()

# Instantiates a connection to the database
if __name__ == '__main__':
    print()
    # Scraper containers will be instantiated based on the number of websites fetched using the docker python API
    ## Get list of websites to be scraped
    url_dict = {
        'dubizzle' : 'https://www.dubizzle.com.om/en/vehicles/cars-for-sale', 
    }
    
    ## Initialize a list for scraper functions to be started
    scraper_list = []

    for k, v in url_dict.items():
        scraper_instance = Process(target=scraper.start, args=(k, v))
        scraper_list.append(scraper_instance)
        scraper_instance.start()
        info(f'Started {k} scraper instance')
        
    for s in scraper_list:
        s.join()
    success('Scraping finished')
    

    csv_dict = {
        os.path.splitext(os.path.basename(k))[0] : k for k in glob.glob(f'{WORKDIR}/src/stg/*')
    }

    preprocessor_list = []

    for k, v in csv_dict.items():
        preprocessor_instance = Process(target=preprocessor.start, args=(k, v))
        preprocessor_list.append(preprocessor_instance)
        preprocessor_instance.start()
        info(f'Started {k} preprocessor instance')
        
    for s in preprocessor_list:
        s.join()
    success('Preprocessing finished')