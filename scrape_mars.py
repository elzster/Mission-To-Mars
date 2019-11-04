from splinter import Browser
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
import pandas as pd

#Launches Website
url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(url)
html=browser.html

#### Sets up the Necessary Variables for the Most Recent News Article.
#need to get a variable for 'news_title' and 'news_p'
soup = bs(html, 'html.parser')
latest_news_date = (soup.find_all('div', class_="list_date"))[0].get_text()
latest_news_title = (soup.find_all('div', class_='content_title'))[0].get_text()
latest_news_paragraph = (soup.find_all('div', class_='article_teaser_body'))[0].get_text()

#### Set up Scraper for Mars Images from Images Site.
#Launches Website and Parses Data into Beautiful Soup.
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(url)
html=browser.html
soup = bs(html, 'html.parser')
#need to scrape for featured image url, variable featured_image_url
image = (soup.find_all('div', class_='carousel_items')[0].a.get('data-fancybox-href'))

#example of print out
featured = 'https://www.jpl.nasa.gov'+ image
# print(featured)

#### Scrape Mars Weather From Twitter Account
#Launches Website and Parses Data into Beautiful Soup.
url = 'https://twitter.com/marswxreport?lang=en'
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(url)
html=browser.html
soup = bs(html, 'html.parser')
#Save The Tweet of the most Recent Mars Weather String.
mars_weather = (soup.find_all('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')[0].get_text())
#prints most recent variable
# mars_weather

## Scraping Mars Facts Webpage
#Launches Website and Parses Data into Beautiful Soup.
url = 'https://space-facts.com/mars/'
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(url)
html=browser.html
soup = bs(html, 'html.parser')
tables_df = ((pd.read_html(url))[1]).rename(columns={0: "Attribute", 1: "Value"})
#Use Pandas to convert the data to a HTML table string, Along with cleaning out the '\n' string in a function.
html_table = (tables_df.to_html()).replace('\n', '')

### Mars Hemispheres
#cerberus url
url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(url)
html=browser.html
soup = bs(html, 'html.parser')
cerberus_url = (soup.find_all('div', class_='downloads')[0].li.a.get('href'))

#Schiaparelli Hemisphere url
url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(url)
html=browser.html
soup = bs(html, 'html.parser')
schiaparelli_url = (soup.find_all('div', class_='downloads')[0].li.a.get('href'))

#Syrtis Major Hemisphere
url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(url)
html=browser.html
soup = bs(html, 'html.parser')
syrtis_major_url = (soup.find_all('div', class_='downloads')[0].li.a.get('href'))

#Valles Marineris Hemisphere Url
url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(url)
html=browser.html
soup = bs(html, 'html.parser')
valles_marineries_url= (soup.find_all('div', class_='downloads')[0].li.a.get('href'))

#Create a Dictionary of the Title of the Hemispheres with Respective Image Urls
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": valles_marineries_url},
    {"title": "Cerberus Hemisphere", "img_url": cerberus_url},
    {"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_url},
    {"title": "Syrtis Major Hemisphere", "img_url": syrtis_major_url},]

