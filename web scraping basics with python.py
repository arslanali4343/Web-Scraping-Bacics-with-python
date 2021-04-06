# -*- coding: utf-8 -*-


Load in the necessary libraries
"""

pip install beautifulsoup4

import requests

from bs4 import BeautifulSoup as bs

"""## Look the webpage content"""

r= requests.get('https://arslanali4343.github.io/Personal-Portfolio/')

"""## Convert to a beautiful soup page"""

soup = bs(r.content)
print(soup.prettify())

"""## Start using beatiful soup to scrape
# Fina and find out
"""

first_header = soup.find("h2")
first_header

headers = soup.find_all("h2")
print(headers)

"""## pass in a list of elements to look for"""

first_header = soup.find_all(["h1" , "h2"])
first_header

"""## you can pass in attributes to the find / find_all function"""

paragraph = soup.find_all("p" , attrs= {"id" : "paragraph-id"})
paragraph

"""## You can nest find / find_all calls"""

body = soup.find('body')

div = soup.find('div')
header = div.find('h1')
header

"""### we can search specific strings in our find \ find_all calls"""

import re

paragraphs =  soup.find_all("p" , string= re.compile("Some"))
paragraphs
headers = soup.find_all("h2" , string = re.compile("(H|h)eader"))
headers

"""## select (css selection)"""

content = soup.select("p")
content

content = soup.select("div p")
content

paragraphs = soup.select ("h2 ~ p")
paragraphs

bold_text = soup.select("p#paragraph-id b")
bold_text

paragraphs = soup.select("body > p")
print(paragraphs)

for paragraph in paragraphs:
  print(paragraph.select("i"))

"""## Grap by element with specific property"""

soup.select("[align=middle]")

## Load the webpage content
r = requests.get("https://arslanali4343.github.io/Personal-Portfolio/")
# convert to a beautiful soup object
webpage = bs(r.content)
#print out our html
print(webpage.prettify())

"""## Grab all the social links from the webpage

## Do this in at least 3 different ways
"""

links = webpage.select("a")
links

links = webpage.select("ul.socials")
links

links = webpage.select("ul.socials a")
links

links = webpage.select("ul.socials a")
actual_links = [link['href'] for link in links]
actual_links

ulist = webpage.find("ul" , attrs={"class": "socials"})
links = ulist.find_all("a")
links

import pandas as pd
table =  webpage.select("table.hockey-stats")[0]
columns = table.find("thead").find_all("th")
columns_names = [c.string for c in columns]
columns_names

table_rows = []
l = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    l.append(row)
pd.DataFrame(l, columns=["A", "B", ...])

import pandas as pd

table =  webpage.select("table.hockey-stats")[0]
columns = table.find("thead").find_all("th")
columns_names = [c.string for c in columns]

table_rows = table.find("tbody").find_all("tr")
l = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [str(tr.get_text()).strip() for tr in td]
    l.append(row)
    
df = pd.DataFrame(l, columns = columns_names)
df.head()

