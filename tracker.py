from bs4 import BeautifulSoup

with open('scraper.hmtl', 'r') as html_file:
    content = html_file.read()
    print(content)
