from bs4 import BeautifulSoup
import requests

list = []
for i in range(1,35):
    data = requests.get('https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/1').text
    soup = BeautifulSoup(data, 'html.parser')

    # print(soup.prettify())

    tbody = soup.find('tbody')
    for tr in tbody:
        td = tr.find('td', class_='data-table__cell csr-col--school-name')
        list.append(str(td.text)[6:])


for a in list:
    print(a)