#!/usr/bin/env python
# coding: utf-8

# In[40]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from matplotlib.colors import ListedColormap
import seaborn as sns
from sklearn.metrics import confusion_matrix


# In[17]:


df=pd.read_csv('Iris.csv')


# In[18]:


df.head(10)


# In[20]:


df.Species.unique()


# In[21]:


x=df.iloc[:, [1,4]].values


# In[22]:


x


# In[23]:


y=df.iloc[:,5].values


# In[24]:


y


# In[25]:


le=LabelEncoder()
y=le.fit_transform(y)


# In[26]:


y


# In[27]:


x_test, x_train, y_test, y_train=train_test_split(x, y, test_size=0.2)


# In[32]:


classifier=SVC(kernel='linear', random_state=0)
classifier.fit(x_train, y_train)


# In[33]:


y_pred= classifier.predict(x_test)


# In[34]:


y_pred


# In[35]:


y_test


# In[37]:


c=0
e=0
for i in range(0, len(y_test)):
    if(y_pred[i]==y_test[i]):
        c=c+1
    else:
        e=e+1
print("Accuracy-",(c/len(y_test))*100)
print("Error-", (e/len(y_test))*100)


# In[41]:


cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, cmap='Blues', fmt='g', xticklabels=le.classes_, yticklabels=le.classes_)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()


# In[42]:


cm


# In[43]:


x_train


# In[ ]:




