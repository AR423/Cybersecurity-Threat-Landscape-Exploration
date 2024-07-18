import requests
from bs4 import BeautifulSoup
import csv

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

# Save the data as a CSV file
csv_filename = 'data/group_info.csv'
csv_header = ['name', 'associated groups', 'description']

with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_header)
    writer.writeheader()
    for info in group_info_list:
        writer.writerow(info)

print(f"Data saved to {csv_filename}")