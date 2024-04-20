#!/usr/bin/env python
# coding: utf-8

# In[35]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
print('Import successful')


# In[36]:


df=pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')


# In[37]:


df.head(10)


# In[38]:


df.tail(10)


# In[39]:


df.shape


# In[41]:


df['Amount'].fillna(df['Amount'].mean(), inplace=True)


# In[42]:


df.info()


# In[43]:


df = df.drop(columns=columns_to_drop, errors='ignore')


# In[44]:


df.info()


# In[45]:


df['Gender'].value_counts()


# In[46]:


df['Age Group'].value_counts()


# In[47]:


df['Age'].value_counts()


# In[49]:


df['Marital_Status'].value_counts()


# In[50]:


df['State'].value_counts()


# In[51]:


df['Zone'].value_counts()


# In[52]:


df['Occupation'].value_counts()


# In[53]:


df['Product_Category'].value_counts()


# In[54]:


df['Orders'].value_counts()


# In[61]:


print("Maximum amount spent-", df['Amount'].max())
print()
print("Minimum amount spent-", df['Amount'].min())


# In[62]:


df.describe()


# In[65]:


ax=sns.countplot(data=df, x='Age Group', hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[79]:


plt.figure(figsize=(8, 6))
ax = sns.barplot(data=df, x='Gender', y='Amount', estimator=sum, ci=None)
plt.title('Total Amount Spent by Gender')
plt.xlabel('Gender')
plt.ylabel('Total Amount Spent')

# Add labels on top of each bar
for p in ax.patches:
    ax.annotate('{:.2f}'.format(p.get_height()), 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', fontsize=10, color='black', xytext=(0, 5), 
                textcoords='offset points')

plt.show()


# In[77]:


plt.figure(figsize=(15, 10))
ax = sns.barplot(data=df, x='State', y='Amount', estimator=sum, ci=None)
plt.title('Total Amount Spent by State')
plt.xlabel('State')
plt.ylabel('Total Amount Spent')
plt.xticks(rotation=45)  


for p in ax.patches:
    ax.annotate('{:.2f}'.format(p.get_height()), 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', fontsize=10, color='black', xytext=(0, 5), 
                textcoords='offset points')

plt.tight_layout()  
plt.show()


# In[85]:


state_sales=df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(5)
sns.set(rc={'figure.figsize':(10,10)})
sns.barplot(data=state_sales, x='State', y='Orders')


# In[86]:


plt.figure(figsize=(8, 6))
ax = sns.countplot(data=df, x='Gender', hue='Marital_Status')
plt.title('Marital Status by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')

for p in ax.patches:
    ax.annotate('{:.0f}'.format(p.get_height()), 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', fontsize=10, color='black', xytext=(0, 5), 
                textcoords='offset points')

plt.show()


# In[92]:


plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='Occupation', y='Amount', hue='Gender', estimator=sum, ci=None)
plt.title('Total Amount Spent by Occupation and Gender')
plt.xlabel('Occupation')
plt.ylabel('Total Amount Spent')
plt.xticks(rotation=45)  
plt.legend(title='Gender')
plt.tight_layout()  
plt.show()


# In[94]:


it_healthcare_aviation = df[df['Occupation'].isin(['IT Sector', 'Healthcare', 'Aviation'])]

plt.figure(figsize=(10, 6))
ax = sns.barplot(data=it_healthcare_aviation, x='Occupation', y='Amount', hue='Gender', ci=None)
plt.title('Amount Spent in IT Sector, Healthcare, and Aviation by Gender')
plt.xlabel('Occupation')
plt.ylabel('Total Amount Spent')

for p in ax.patches:
    ax.annotate('{:.2f}'.format(p.get_height()), 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', fontsize=10, color='black', xytext=(0, 5), 
                textcoords='offset points')

plt.xticks(rotation=45)  
plt.legend(title='Gender')
plt.tight_layout()  
plt.show()


# In[96]:


print("The most spending was done by married women working in IT sector and Aviation.")
print("")
print("The state of Uttar Pradesh saw highest number of orders, followed by Maharashtra and Karnatak.")
print("")
print("The product categories which were sold are- Clothing & Apparel,Food and Electronics & Gadgets")


# In[ ]:




