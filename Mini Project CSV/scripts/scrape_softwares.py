import requests
from bs4 import BeautifulSoup
import csv

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

# Save the data as a CSV file
csv_filename = 'data/software_info.csv'
csv_header = ['type', 'name', 'associated software', 'description']

with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_header)
    writer.writeheader()
    for info in software_info_list:
        writer.writerow(info)

print(f"Data saved to {csv_filename}")