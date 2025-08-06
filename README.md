# Oman Online Market Scraper
This project serves as a proof-of-concept showcasing the ability to scrape data off of Oman-based or available-in-Oman e-commerce websites. The data scraped off these websites can then be used in data analytics or machine learning so that it aids end users (consumers) in the decision-making processes in purchasing items/properties.

This project will be divided in two segments/phases. The first phase will be for data collection and data modeling, where the data pipeline will be implemented to do so. In the second phase, the data collected will go through analysis to extract insights and machine learning for constant insights extraction.

Other than whats mentioned above, proper orchestration, CI/CD and MLOps processes will be implemented in the future.

# Data Collection/Modeling
![Phase One](https://github.com/WarriorM0nk/oman-online-markets-scraper/docs/diagrams/phase_one.png)

- [ ] **Master Script**: To act as an orchestrator that will retrieve website-specific configuration and also instantiate containers based on the number of websites applicable for scraping.
- [ ] **Configuration Database**: To have a different set of configuration data based on the HTML structure and items advertised on each website.
- [ ] **Scraper**: Has a unified structure that only changes based on the configuration that the *Master Script* provides.
- [ ] **Validator**: To validate that the data extracted does not exist on the database.
- [ ] **Preprocessor** To preprocess data before being loaded into a database.
- [ ] **Items Database** To store data after preprocessing.

# Data Analysis/Machine Learning
**TBA**

# Material
**TBA**
