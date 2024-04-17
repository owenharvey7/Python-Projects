# 16
# Web Scraping Challenge:
# Scrape and print the titles of articles from a news website.
import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

titles = soup.find_all(class_='indicate-hover')
titles_list = []

# Get all the titles into a list
for title in titles:
    titles_list.append(title.get_text())


# Get rid of the last 6 titles which are not articles
titles_list = titles_list[:-6]

# Print a title for the list
print("\nTitles of Articles from The New York Times\n")

# Print the list with a numbered format
for i, title in enumerate(titles_list):
    print(f"{i+1}. {title}\n")



