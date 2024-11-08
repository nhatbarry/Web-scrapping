import requests
from bs4 import BeautifulSoup

url = 'https://wakatime.com/leaders/language/html?page=1&country_code=VN'
response = requests.get(url)


if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_='table leaders')
    rows = table.find_all('tr')
    for row in rows[1:]:
        cols = row.findAll('td')
        rank = cols[0].text
        name = cols[1].text
        hours = cols[2].text
        daily = cols[3].text
        language = cols[4].text
        print(f"Rank {rank}:{name}\
              \nHours of coded: {hours}\
              \nDaily Average: {daily}\
              \nLanguage used: {language}\n\n")