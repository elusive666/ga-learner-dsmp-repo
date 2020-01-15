# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





#Code starts here
data = pd.read_csv(path)

# sns.distplot(data.Rating)
# plt.show()

data = data[data.Rating <= 5]
plt.hist(data.Rating)
plt.show()

#Code ends here


# --------------
# code starts here
total_null = data.isnull().sum()
percent_null = (total_null/len(data))
missing_data = pd.concat([total_null, percent_null], keys=['Total','Percent'], axis=1)
data = data.dropna(axis = 0)
total_null_1 = data.isnull().sum()
percent_null_1 = (total_null_1/len(data))
missing_data_1 = pd.concat([total_null_1, percent_null_1],keys=['Total','Percent'], axis=1)
print(missing_data_1)
# code ends here


# --------------

#Code starts here

sns.catplot(x="Category",y="Rating",data=data, kind="box", height = 10)
plt.xticks(rotation = 90)
plt.title('Rating vs Category [BoxPlot]')
plt.show()

#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
print(data.Installs.value_counts())
def cleanInstall(tempStr):
    tempStr = tempStr.replace(',', '')
    tempStr = tempStr.replace('+', '')
    return tempStr
data['Installs'] = data['Installs'].apply(lambda x : cleanInstall(str(x)))
data['Installs'] = data['Installs'].astype(int)

le = LabelEncoder()
data['Installs'] = le.fit_transform(data['Installs'])

sns.regplot(x='Installs', y='Rating', data=data)
plt.title('Rating vs Installs [RegPlot]')
plt.show()



#Code ends here



# --------------
#Code starts here

# print(data.Price.value_counts())
data['Price'] = data['Price'].str.replace('$', '')
data['Price'] = data['Price'].astype(float)
print(data.Price.value_counts())
sns.regplot(x="Price", y="Rating", color = 'teal',data=data)
#Setting the title of the plot
plt.title('Rating vs Price[RegPlot]',size = 20)

#Code ends here


# --------------

#Code starts here

data['Genres'] = data['Genres'].apply(lambda x : str(x).split(';')[0])
data.head()
gr_mean = data.groupby(['Genres'], as_index=False)[['Rating']].mean()
gr_mean.describe()
gr_mean = gr_mean.sort_values(by='Rating')
print(gr_mean.iloc[0])
print(gr_mean.iloc[-1])


#Code ends here


# --------------

#Code starts here

data['Last Updated'].head()
data['Last Updated'] = pd.to_datetime(data['Last Updated'])
max_date = data['Last Updated'].max()
data['Last Updated Days'] = (max_date - data['Last Updated']).dt.days
sns.regplot(x="Last Updated Days", y="Rating", data=data)
plt.title('Rating vs Last Updated [RegPlot]')
plt.show()
#Code ends here


