from bs4 import BeautifulSoup
import re
import requests
import shutil

html_page = requests.get('https://github.com/Evavic44/portfolio-ideas?tab=readme-ov-file')
soup = BeautifulSoup(html_page.content, 'html.parser')

website_links = [td.find("a") for td in soup.find_all("table")[1].find_all("td")[2::5]]
img_tags = [td.find("a") for td in soup.find_all("table")[1].find_all("td")[1::5]]

for web_link, img_tag in zip(website_links, img_tags):
    r = requests.get(img_tag["href"], stream = True)
    if r.status_code == 200:
        with open(web_link.text + ".png", 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    else:
        print(web_link.text + " failed")
