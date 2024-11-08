import csv
import requests
from bs4 import BeautifulSoup

url = 'https://wakatime.com/leaders/language/html?page=1&country_code=VN'
response = requests.get(url)


import csv
from bs4 import BeautifulSoup

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_='table leaders')
    rows = table.find_all('tr')
    data = []

    for row in rows[1:]:
        cols = row.find_all('td')
        rank = cols[0].text.strip()
        name = cols[1].text.strip()
        hours = cols[2].text.strip()
        daily = cols[3].text.strip()
        language = cols[4].text.strip()
        
        data.append({
            'rank': rank,
            'name': name,
            'hours of coded': hours,
            'daily average': daily,
            'language used': language
        })

    with open('leaderboard.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['rank', 'name', 'hours of coded', 'daily average', 'language used'])
        writer.writeheader()
        writer.writerows(data)
        print('this shit is done')
