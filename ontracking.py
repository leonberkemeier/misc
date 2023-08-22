from bs4 import BeautifulSoup

import requests

html_text=requests.get('https://www.tripadvisor.de/Restaurants-g187382-Muenster_North_Rhine_Westphalia.html').text
soup = BeautifulSoup(html_text, 'lxml')
restaurants = soup.find_all('div',class_ = 'RfBGI')

# print(restaurants)
print(html_text)