import csv
import requests
from bs4 import BeautifulSoup

url = 'https://www.ola.state.md.us/Search/Report?keyword=&agencyId=&dateFrom=&dateTo='
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html)
table = soup.find('tbody')

list_of_rows = []
for row in table.find_all('tr'):
    list_of_cells = []
    for cell in row.find_all('td'):
        if cell.find('a'):
            list_of_cells.append(cell.find('a')['href'])
        text = cell.text.strip()
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("./reports.csv", "w")
writer = csv.writer(outfile)
#writer.writerow(["Last", "First", "Middle", "Gender", "Race", "Age", "City", "State"])
writer.writerows(list_of_rows)
