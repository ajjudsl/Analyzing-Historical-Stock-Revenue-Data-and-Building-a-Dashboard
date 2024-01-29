#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf


# In[2]:


get_ipython().system('pip install yfinance')


# In[3]:


python -m pip install yfinance


# In[4]:


get_ipython().system('pip install yfinance')


# In[5]:


get_ipython().system('pip install pandas')


# In[6]:


get_ipython().system('pip install requests')


# In[7]:


get_ipython().system('pip install bs4')


# In[8]:


get_ipython().system('pip install plotly')


# In[9]:


import yfinance as yf


# In[11]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
import plotly.subplots import make_subplots


# In[12]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[13]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[14]:


tesla = yf.Ticker('TSLA')


# In[15]:


tesla_data = tesla.history(period="max")


# In[16]:


tesla_data.reset_index(inplace=True)
tesla_data.head(5)


# In[17]:


url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data = requests.get(url).text


# In[18]:


soup = BeautifulSoup(html_data, "html5lib")
print(soup.prettify())


# In[19]:


tesla_revenue = pd.DataFrame(columns = ["Date","Revenue"])

for table in soup.find_all('table'):
    if table.find('th').getText().startswith("Tesla Quarterly Revenue"):
        for row in table.find("tbody").find_all("tr"):
            col = row.find_all("td")
            if len(col) != 2: continue
            Date = col[0].text
            Revenue = col[1].text.replace("$","").replace(",","")
               
            tesla_revenue = tesla_revenue.append({"Date":Date, "Revenue":Revenue}, ignore_index=True)


# In[20]:


tesla_revenue.dropna(axis=0, how='all', subset=['Revenue'])
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]


# In[21]:


tesla_revenue.tail(5)


# In[22]:


gme = yf.Ticker('GME')


# In[23]:


gme_data = gme.history(period = "max")


# In[24]:


gme_data.reset_index(inplace=True)
gme_data.head(5)


# In[25]:


url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data = requests.get(url).text


# In[26]:


soup = BeautifulSoup(html_data, "html5lib")
print(soup.prettify())


# In[27]:


gme_revenue = pd.DataFrame(columns = ["Date","Revenue"])

for table in soup.find_all('table'):
    if table.find('th').getText().startswith("GameStop Quarterly Revenue"):
        for row in table.find("tbody").find_all("tr"):
            col = row.find_all("td")
            if len(col) != 2: continue
            Date = col[0].text
            Revenue = col[1].text.replace("$","").replace(",","")
               
            gme_revenue = gme_revenue.append({"Date":Date, "Revenue":Revenue}, ignore_index=True)


# In[28]:


gme_revenue.tail(5)


# In[30]:


make_graph(tesla_data, tesla_revenue,'Tesla')


# In[31]:


make_graph(gme_data, gme_revenue, 'GameStop')


# In[ ]:




