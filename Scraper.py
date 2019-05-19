# The first step is to import the requests library and download the Boone County webpage.
import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)
print("Response code: {}".format(response.status_code))
html_text = response.content
# print(html_text)

soup = BeautifulSoup(html_text, features="html.parser")
titles = []
for title in soup.find_all('a', title=True):
    titles.append(title)
print(titles)

print("This message was added to test commit on pycharm")
