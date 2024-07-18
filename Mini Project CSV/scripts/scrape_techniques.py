import requests
from bs4 import BeautifulSoup
import csv

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

# Save the data as a CSV file
csv_filename = 'data/technique_info.csv'
csv_header = ['type', 'name', 'description']

with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_header)
    writer.writeheader()
    for info in technique_info_list:
        writer.writerow(info)

print(f"Data saved to {csv_filename}")