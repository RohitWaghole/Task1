import requests
from bs4 import BeautifulSoup
import json

# conecting to the target URL to scrape
url = 'https://en.wikipedia.org/wiki/Angular_(web_framework)'

# access the HTML
page = requests.get(url)
htmlContent = page.content

# Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')

# Getting the title of the wikipedia page
title = soup.title.string

# Fetching all the versions in the History sections 
headings = [i.string for i in  soup.find_all('span', class_='mw-headline')]

# Fetching all the links in the references section
references = [i.get('href') for i in soup.find_all('a', class_='external text')]

content = [
    {
    'heading': headings,
    'reference': references
    }
]


data = {
    'title': title,
    'url': url,
    'content': content
}


# dumping the data into the json file
with open("data.json", "w") as f:
    json.dump(data, f)

# dumping the data into the text file
with open("data.txt", "w") as f:
    json.dump(data, f)



print("successfully dumped")