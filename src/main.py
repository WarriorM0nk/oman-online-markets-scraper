from multiprocessing import Process
import scraper

# Instantiates a connection to the database
if __name__ == '__main__':
    # Scraper containers will be instantiated based on the number of websites fetched using the docker python API
    ## Get list of websites to be scraped
    url_dict = {
        'dubbizle' : 'https://www.dubizzle.com.om/en/vehicles/cars-for-sale', 
    }
    
    ## Initialize a list for scraper functions to be started
    scraper_list = []

    for k, v in url_dict.items():
        scraper_instance = Process(target=scraper.start, args=(v, k))
        scraper_list.append(scraper_instance)
        scraper_instance.start()
        
    for s in scraper_list:
        s.join()
                    