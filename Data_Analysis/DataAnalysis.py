import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv('hotel_booking.csv')

df=df.drop(['name', 'email', 'phone-number', 'credit_card'], axis=1)

print(df.head(25))
print()
print('-'*50)
print()
print(df.tail(25))
print('-'*50)
print()
print(df.info())

df['reservation_status_date']=pd.to_datetime(df['reservation_status_date'])

for col in df.describe(include='object').columns:
  print(col)
  print(df[col].unique())
  print('-'*50)

print(df.isnull().sum())
print('-'*50)
print()

df.drop(['company', 'agent'], axis=1, inplace=True)
df.dropna(inplace= True)
print(df.isnull().sum())
print('-'*50)
print()

print(df.describe())
print('-'*50)
print()

print('Detecting and removing outliers...')
while(True):
  print('Select 1 to show graph and 2 to exit')
  a=int(input("Enter your choice-"))
  if(a==1):
    print(df['adr'].plot(kind='box'))
    plt.show()
  elif(a==2):
    break
print('-'*50)
print()

df=df[df['adr']<5000]
cancelled_percent=df['is_canceled'].value_counts(normalize=True)
print(cancelled_percent)
print('-'*50)
print()

while(True):
  print('Select 1 to show graph and 2 to exit')
  a=int(input("Enter your choice-"))
  if(a==1):
    plt.figure(figsize=(5,5))
    plt.title("Reservation status count")
    plt.bar(['Not cancelled', 'Cancelled'], df['is_canceled'].value_counts())
    plt.show()
  elif(a==2):
    break
print('-'*50)
print()

while(True):
  print('Select 1 to show graph and 2 to exit')
  a=int(input("Enter your choice-"))
  if(a==1):
    plt.figure(figsize=(10,10))
    graph1=sns.countplot(x='hotel', hue='is_canceled', data=df, palette='Blues')
    legend_labels,_= graph1.get_legend_handles_labels()
    plt.title("Reservation status in hotels", size=15)
    plt.xlabel('Hotel')
    plt.ylabel('No. of reservations')
    plt.show()
  elif(a==2):
    break
print('-'*50)
print()

resort_hotel=df[df['hotel']=='Resort Hotel']
print(resort_hotel['is_canceled'].value_counts(normalize=True))
print('-'*50)
print()

city_hotel=df[df['hotel']=='City Hotel']
print(city_hotel['is_canceled'].value_counts(normalize=True))
print('-'*50)
print()

resort_hotel= resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel= city_hotel.groupby('reservation_status_date')[['adr']].mean()

while(True):
  print('Select 1 to show graph and 2 to exit')
  a=int(input("Enter your choice-"))
  if(a==1):
    plt.figure(figsize=(20,0))
    plt.title("Average daily rate in city and resort hotels", fontsize=25)
    plt.plot(resort_hotel.index, resort_hotel['adr'], label='Resort hotel')
    plt.plot(city_hotel.index, city_hotel['adr'], label='City hotel')
    plt.legend(fontsize=20)
    plt.show()
  elif(a==2):
    break
print('-'*50)
print()

while(True):
  print('Select 1 to show graph and 2 to exit')
  a=int(input("Enter your choice-"))
  if(a==1):
    df['month']=df['reservation_status_date'].dt.month
    plt.figure(figsize=(15,10))
    ax1=sns.countplot(x='month', hue='is_canceled', data=df, palette='bright')
    legend_labels,_=ax1.get_legend_handles_labels()
    ax1.legend(bbox_to_anchor=(1,1))
    plt.title('Reservation status per month', size=20)
    plt.xlabel('Month')
    plt.ylabel('Reservations made')
    plt.legend(['Not canceled', 'Canceled'])
    plt.show()
  elif(a==2):
    break
print('-'*50)
print()

while(True):
  print('Select 1 to show graph and 2 to exit')
  a=int(input("Enter your choice-"))
  if(a==1):
    df['month']=df['reservation_status_date'].dt.month
    plt.figure(figsize=(15,10))
    plt.title('ADR per month', fontsize=25)
    filtered_df = df[df['is_canceled'] == 1].groupby('month')[['adr']].sum().reset_index()
    sns.barplot(x='month', y='adr', data=filtered_df)
    plt.show()
  elif(a==2):
    break
print('-'*50)
print()

cancelled_data=df[df['is_canceled']==1]
top_10_country= cancelled_data['country'].value_counts()[:10]
while(True):
  print('Select 1 to show graph and 2 to exit')
  a=int(input("Enter your choice-"))
  if(a==1):
    plt.figure(figsize=(15,10))
    plt.title('Top 10 countries with reservation with reservation canceled')
    plt.pie(top_10_country, autopct='%.2f', labels=top_10_country.index)
    plt.show()
  elif(a==2):
    break
print('-'*50)
print()

print(df['market_segment'].value_counts())
print('-'*50)
print()

print(cancelled_data['market_segment'].value_counts(normalize=True))
print('-'*50)
print()

