# 5. program a code which download a webpage contains a table using Request library, then parse the page using
# Beautifusoup library. You should save all the information of the table in a file.
# Sample input: https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2015
# Sample output: Save the table in this link into a file

import requests # Importing Requests Library

# Use of requests.get to download the webpage
page = requests.get("https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2015")
print(page) # Printing the webpage as an object
page.status_code # To know the status code of the webpage, 200 means the download was sucessfull
page.content # Printing the Html content of the page

# Parsing the webpage withe BeautifulSoup
from bs4 import BeautifulSoup # Importing BeautifulSoup4 from bs4
soup = BeautifulSoup(page.content, 'html.parser') # PArsing the html pages in the page content

print(soup.h1.text) # Printing the titles of the object soup

print(soup.title.text) # To print the texts in the title

for link in soup.find_all('a'): # Printing the links

    print(link.get('href'))
