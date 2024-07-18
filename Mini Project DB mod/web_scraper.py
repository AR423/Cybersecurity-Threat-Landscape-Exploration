import requests
from bs4 import BeautifulSoup
import sqlite3



def insert_data_into_db(table_name, data):
    conn = sqlite3.connect('scraped_data.db')
    cursor = conn.cursor()
    
    if table_name == "groups":
        for row in data:
            cursor.execute(f'INSERT INTO {table_name} (Associated_groups, Name, Description) VALUES (?, ?, ?)', 
                           (row["associated groups"], row["name"], row["description"]))
    elif table_name == "softwares":
        for row in data:
            cursor.execute(f'INSERT INTO {table_name} (Associated_softwares, Name, Description, Type) VALUES (?, ?, ?, ?)', 
                           (row["associated software"], row["name"], row["description"], row["type"]))
    elif table_name == "techniques":
        for row in data:
            cursor.execute(f'INSERT INTO {table_name} (Name, Description, Type) VALUES (?, ?, ?)', 
                           (row["name"], row["description"], row["type"]))
    else:
        print("Invalid table name!")
    
    conn.commit()
    conn.close()



def groups_scraper():

    url = 'https://attack.mitre.org/versions/v15/groups/' 
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')
    group_info_list = []
    rows = soup.find_all('tr')

    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 4:
            group_id = columns[0].text.strip()
            name = columns[1].text.strip()
            associated_groups = columns[2].text.strip()
            description = columns[3].find('p').text.strip()

            group_info = {
                "name": name,
                "associated groups": associated_groups,
                "description": description,
            }
            
            group_info_list.append(group_info)
    
    insert_data_into_db('groups', group_info_list)



def softwares_scraper():

    def classify_software(description):
        """
        Classify the software type based on its description.
        """

        malware_keywords = ["malware", "malicious", "trojan", "virus", "worm", "exploit", "backdoor", "adware", "spyware", "ransomware", "remote access tool"]
        
        for keyword in malware_keywords:
            if keyword.lower() in description.lower():
                return "Malware"
        
        return "Tool"

    url = 'https://attack.mitre.org/versions/v15/software/' 
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')
    software_info_list = []
    rows = soup.find_all('tr')

    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 4:
            software_id = columns[0].text.strip()
            name = columns[1].text.strip()
            associated_software = columns[2].text.strip()
            description = columns[3].find('p').text.strip()
            software_type = classify_software(description)

            software_info = {
                "type": software_type,
                "name": name,
                "associated software": associated_software,
                "description": description,
            }
            
            software_info_list.append(software_info)
    
    insert_data_into_db('softwares', software_info_list)



def techniques_scraper():

    url = 'https://attack.mitre.org/versions/v15/techniques/enterprise/'
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')
    technique_info_list = []
    rows = soup.find_all('tr')

    for row in rows:
        # Determine the type of technique (technique or sub-technique)
        row_class = row.get('class', [])
        
        if row_class == ['sub', 'technique']:
            technique_type = 'sub-technique'
            columns = row.find_all('td')
            if len(columns) >= 4:
                id_text = columns[1].find('a').text.strip() if columns[1].find('a') else columns[1].text.strip()
                name = columns[2].text.strip()
                description = columns[3].text.strip()
        
        elif row_class == ['technique']:
            technique_type = 'technique'
            columns = row.find_all('td')
            if len(columns) >= 3:
                id_text = columns[0].find('a').text.strip() if columns[0].find('a') else columns[0].text.strip()
                name = columns[1].text.strip()
                description = columns[2].text.strip()

        else:
            continue

        technique_info = {
            "type": technique_type,
            "name": name,
            "description": description
        }
        
        technique_info_list.append(technique_info)
    
    insert_data_into_db('techniques', technique_info_list)



groups_scraper()
softwares_scraper()
techniques_scraper()