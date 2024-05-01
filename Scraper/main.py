# In this part of the project I will be extracting articles
# From Shopify Dev blog

# Python version - 3.8.10
# Imports
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from urllib.parse import urljoin


# Scrape function should return object which contains, company name, url of article, title of article,
def scrape(url: str, articleTag) -> object:
    data = requests.get(url) # Get html document
    html = BeautifulSoup(data.text, 'html.parser') # Turn html into object
    articles = html.select(articleTag) # Select all acticles
    articles_data = []

    for article in articles:

        title = article.select('h2')[0].get_text() # Get article
        link_relative = article.select('a.article--index__link')[0].get('href') # Get relative link to article
        link_absolute = urljoin("https://shopify.engineering", link_relative) # Get absolute link to article
        image = article.select('img')[0].get('data-srcset') # Get image of article
        articles_data.append({"title": title.replace("\n", ""), "link": link_absolute, "image": image}) # Append string to key and remove \n from string

    return articles_data

# Implement helper function that adds all available pages and traverse throught them
# If not article element found on .....pages=n, then stop iteration and return number of available pages



pprint(scrape("https://shopify.engineering/topics/development", "article"))