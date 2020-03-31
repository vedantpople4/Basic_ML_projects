#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import datetime
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)


# In[3]:


BAC = data.DataReader("BAC", 'google', start, end)
C = data.DataReader("C", 'google', start, end)
GS = data.DataReader("GS", 'google', start, end)
JPM = data.DataReader("JPM", 'google', start, end
MS = data.DataReader("MS", 'google', start, end)
WFC = data.DataReader("WFC", 'google', start, end)


# In[4]:


df = data.DataReader(['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC'],'google', start, end)


# In[5]:


tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']


# In[6]:


bank_stocks = pd.concat([BAC, C, GS, JPM, MS, WFC],axis=1,keys=tickers)


# In[7]:


bank_stocks.columns.names = ['Bank Ticker','Stock Info']


# In[8]:


bank_stocks.head()


# In[9]:


bank_stocks.xs(key='Close',axis=1,level='Stock Info').max()


# In[10]:


returns = pd.DataFrame()


# In[11]:


for tick in tickers:
    returns[tick+' Return'] = bank_stocks[tick]['Close'].pct_change()
returns.head()


# In[13]:


#returns[1:]
import seaborn as sns
sns.pairplot(returns[1:])


# In[14]:


returns.idxmin()


# In[15]:


returns.idxmax()


# In[16]:


returns.std()


# In[17]:


returns.ix['2015-01-01':'2015-12-31'].std() 


# In[18]:


sns.distplot(returns.ix['2015-01-01':'2015-12-31']['MS Return'],color='green',bins=100)


# In[19]:


sns.distplot(returns.ix['2008-01-01':'2008-12-31']['C Return'],color='red',bins=100)


# In[20]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')


import plotly
import cufflinks as cf
cf.go_offline()


# In[21]:


for tick in tickers:
    bank_stocks[tick]['Close'].plot(figsize=(12,4),label=tick)
plt.legend()


# In[22]:


bank_stocks.xs(key='Close',axis=1,level='Stock Info').plot()


# In[24]:


plt.figure(figsize=(12,6))
BAC['Close'].ix['2008-01-01':'2009-01-01'].rolling(window=30).mean().plot(label='30 Day Avg')
BAC['Close'].ix['2008-01-01':'2009-01-01'].plot(label='BAC CLOSE')
plt.legend()


# In[25]:


sns.heatmap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)


# In[26]:


sns.clustermap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)

