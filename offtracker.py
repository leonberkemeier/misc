from bs4 import BeautifulSoup

with open('scraper.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    stuffs = soup.find_all('div',class_='chart')

    for stuff in stuffs:
        stuff_name = stuff.h2.text.split()[-1]
        stuff_price=stuff.h3.text.split()[-1]
        print(f'{stuff_name} costs {stuff_price}')
