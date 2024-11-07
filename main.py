import requests
from bs4 import BeautifulSoup

url = 'https://www.formula1.com/en/results/2024/drivers'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Lấy dữ liệu từ bảng
drivers_table = soup.find('table', class_='resultsarchive-table')
rows = drivers_table.find_all('tr')

for row in rows[1:]:  # Bỏ qua hàng tiêu đề
    cols = row.find_all('td')
    position = cols[0].text.strip()
    driver = cols[1].text.strip()
    nationality = cols[2].text.strip()
    car = cols[3].text.strip()
    points = cols[4].text.strip()
    print(f"{position}: {driver} - {nationality} - {car} - {points} points")