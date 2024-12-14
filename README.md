# Cybersecurity_Threat_Landscape_Exploration
A web scraping mini project for cybersecurity analysis using Python performed under the guidance of RHYM technologies

In this repository, there are 2 folders: CSV and DB, indicating the 2 methods in which the scraped data was displayed on the web. The python scripts scraped data from 3 URLs 
(1. https://attack.mitre.org/versions/v15/groups/
2. https://attack.mitre.org/versions/v15/software/
3. https://attack.mitre.org/versions/v15/techniques/enterprise/) 
and stored them in separate csv files or separate tables in a database. The scraped data from these was then manipulated to be viewed on a local webpage using REST APIs.

To view the webpages, open the folder's path in terminal on your system and run app.py. A successful execution will give a development server URL which on pasting in a browser will lead to the respective webpage.

There is another functionality of automated scraping through scheduling that can be implemented in which the python script(s) scrape data and update the database regularly. The commands for the same can be seen in automated_scraping_ss.jpg in the DB folder, and are quite self-explanatory.
