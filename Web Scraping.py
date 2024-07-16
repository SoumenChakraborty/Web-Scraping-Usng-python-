#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install beautifulsoup4 requests


# In[15]:


import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_India'

# Send a GET request to the URL
response = requests.get(url)

# Parse the content of the response with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the 2023 Forbes list
# Usually, tables on Wikipedia pages have the class "wikitable"
tables = soup.find_all('table', {'class': 'wikitable'})

# Assuming the first table is the one we want (you may need to adjust this index)
forbes_table = tables[0]

# Extract table headers
headers = []
for header in forbes_table.find_all('th'):
    headers.append(header.get_text(strip=True))

# Extract table rows
rows = []
for row in forbes_table.find_all('tr')[1:]:  # Skip the header row
    cells = row.find_all(['td', 'th'])
    rows.append([cell.get_text(strip=True) for cell in cells])

# Print the headers and rows
print(headers)
for row in rows:
    print(row)


# In[16]:


import pandas as pd


# In[17]:


df = pd.DataFrame(columns = headers, data = rows)


# In[18]:


df


# In[19]:


df.to_csv(r"C:\Users\Soumen Chakraborty\Desktop\IVY_PRO\Python\Python Datasets\Largest Companies_India.csv", index = False)


# In[ ]:




