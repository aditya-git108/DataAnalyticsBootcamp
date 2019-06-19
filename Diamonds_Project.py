#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


location = "datasets/diamonds.csv"
df = pd.read_csv(location)


# In[7]:

#Make a heatmap to find which variables have most correlation
corr = df.corr()
sns.heatmap(corr, vmin=-1, annot=True)


# In[10]:


#Make a scatterplot of Price against Carat and compare it with the different cuts
sns.lmplot(x='carat', y='price', data=df, 
           fit_reg=True, #include regression line
           hue='cut') 


# In[49]:

#Make data frames for each cut with all of the respective prices
price_cut_df = df[["cut","price"]]

ideal_prices_df = price_cut_df[price_cut_df.cut == "Ideal"]

premium_prices_df = price_cut_df[price_cut_df.cut == "Premium"]

good_prices_df = price_cut_df[price_cut_df.cut == "Good"]

very_good_prices_df = price_cut_df[price_cut_df.cut == "Very Good"]

fair_prices_df = price_cut_df[price_cut_df.cut == "Fair"]


# In[50]:

#Make data frame for average prices each cut

avg_ideal = ideal_prices_df.mean()
avg_premium = premium_prices_df.mean()
avg_very_good = very_good_prices_df.mean()
avg_good = good_prices_df.mean()
avg_fair = fair_prices_df.mean()

quality = ["Ideal", "Premium", "Very Good", "Good", "Fair"]
avg_price = [3457.54197, 4584.257704, 3981.759891, 3928.864452, 4358.757764]
MeanCut = list(zip(quality,avg_price))

price_cut_df2 = pd.DataFrame(data=MeanCut, columns = ["Cut", "Avg Price"])
price_cut_df2


# In[46]:


#create a bar plot of the average prices against the different cuts
sns.barplot(x='Cut', y = "Avg Price",
              data=price_cut_df2)


# In[52]:

#Make a data frame for all of the ideal cut diamonds, and then another dataframe
#where the only other category kept is depth
ideal_df = df[df.cut == "Ideal"]
ideal_depth_df = ideal_df[["cut", "depth"]]


# In[56]:


#Make a violin plot to look at the distribution of the depth
#values of the ideal cut diamonds
sns.violinplot(x='cut', y='depth', data=ideal_depth_df)


# In[55]:


ideal_depth_df.describe()


# In[ ]:




