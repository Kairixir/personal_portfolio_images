from bs4 import BeautifulSoup
import re
import requests

html_page = requests.get('https://github.com/Evavic44/portfolio-ideas?tab=readme-ov-file')
soup = BeautifulSoup(html_page.content, 'html.parser')

website_links = soup.find_all("table")[1].find_all("td")[2::5]
img_tags = soup.find_all("table")[1].find_all("a", target="_blank", href = re.compile("png$|user"))

for web_tag, img_tag in zip(website_links, img_tags):
    pass
