#!/usr/bin/env python
# coding: utf-8

# In[271]:


import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time


# In[644]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://mars.nasa.gov/news/'
browser.visit(url)
html = browser.html
soup = bs(html, 'html.parser')


# In[257]:


news_title = soup.article.find('div', class_='content_title').a.text
news_p = soup.article.find('div', class_='article_teaser_body').text
# for story in stories:
#     try:
#         title = story.find('a')
#         titles = title.text
#         print(titles)
#     except AttributeError as e:
#         print(e)


print(news_title)
print(news_p)


# In[470]:


jpl_url = 'https://www.jpl.nasa.gov/'
browser.visit(jpl_url)
html = browser.html
soup = bs(html)


# In[468]:


browser.links.find_by_partial_text('Images').click()
time.sleep(2)
browser.links.find_by_partial_text('Image').click()
time.sleep(1)
browser.links.find_by_partial_text('Download JPG').click()

featured_image = browser.url
print(featured_image)


# In[475]:


sf_url= 'https://space-facts.com/mars/'
browser.visit(sf_url)
html = browser.html
soup = bs(html)

mars_table = pd.read_html(sf_url)


# In[483]:


mars_df = mars_table[0]
mars_df.head(10)


# In[485]:


html_table = mars_df.to_html()
html_table


# In[645]:


sf_url= 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(sf_url)
html = browser.html
soup = bs(html)


# In[646]:


images= soup.section.find_all('img', class_= 'thumb')

img_urls= []
for i in range(len(images)):
    img_dict= {}
    browser.find_by_css('img.thumb')[i].click()
    img_dict['title'] = browser.find_by_tag('h2').text
    img_dict['img_url'] = browser.find_link_by_text("Sample")['href']
    img_urls.append(img_dict)
    browser.back()


# In[648]:


img_urls


# In[ ]:




