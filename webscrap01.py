# script to do simple webscraping
# need to do pop3 install bs4 and pip3 install requests

from bs4 import BeautifulSoup
import requests

# replace URL below with the scrapping URL

result = requests.get("http://www.oreilly.com/free/")

print(result.status_code)

contents = result.content

soup = BeautifulSoup(contents, "lxml")

# Replace with the search string. Here it is finding all book titles and their links

samples = soup.find_all("a", "item-title")

data ={}
for a in samples:
    title = a.string.strip()
    data[title] = a.attrs['href']

print(data)
