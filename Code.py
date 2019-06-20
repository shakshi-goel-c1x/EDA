# STEP 1
# importing the packages
%matplotlib inline      
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import pandas as pd
import numpy as np
import seaborn as sns
import pandas_profiling

# STEP 2
# reading the datasets
impression = pd.read_csv('172.31.4.99_jsonimpr.log.csv')
capacity = pd.read_csv('172.31.4.99_jsoncapacity.log.csv')
click = pd.read_csv('172.31.4.99_jsonclick.log.csv')
pixel_shopclues = pd.read_csv('pixel_json_shopclues-2019-06-07-09_01_06.csv')
pixel = pd.read_csv('pixel_json-2019-06-07-09_00_23.csv')

# STEP 3
# statistical report of each of the datasets
pandas_profiling.ProfileReport(impression)
pandas_profiling.ProfileReport(impression)
pandas_profiling.ProfileReport(impression)
pandas_profiling.ProfileReport(impression)

# STEP 4
# getting the number of rows and columns in the impression dataset
impression.shape

# listing the different column names in the impression dataset
list(impression)

# fetching the first 5 rows of the impression dataset
impression.head()

# fetching the last 5 rows of the impression dataset
impression.tail()

# STEP 5
# getting the measures of central dependency (mean, mode, median) 
# and measures of dispersion (interquartile range, range, standard deviation) 
# of all the columns in the impression dataset
impression.describe(include='all')

# STEP 6
# returns the count of unique values in each column of the impression dataset
impression.nunique()

# STEP 7
# finds the number of null values in each column of the impression dataset
impression.isnull().sum()

# STEP 8
# required columns of the dataset can be selected
d = impression[['CID', 'UUID']]
print(d)
d = pd.DataFrame(d)

# grouping the new dataframe based on CID
impr = d.groupby(d.CID)
for i in impr:
    print(i)
    
# applying lambda function to group unique UUIDs into a list per CID
category = impr.apply(lambda x:x['UUID'].unique())
category = pd.DataFrame(category)
print(category)

# creating a dictionary with CID as key and count of unique UUIDs as value
top = {}
for index,row in category.iterrows():
    top.update({index:0})
    for i in row:
        c = len(i)
    top[index]=c  
print(top)

# sorting the dictionary based on the number of unique UUIDs per CID, in non-increasing order
def sortSecond(val): 
    return val[1]  
topCategory = [ [k,v] for k, v in top.items() ]
topCategory.sort(key = sortSecond, reverse=True)  
print(topCategory) 

# converting the format of the dictionary topCategory
df  = {'CID': [], 'UUID': []}
for i in topCategory:
    df['CID'].append(i[0])
    df['UUID'].append(i[1])
# converting the dictionary to a DataFrame
df = pd.DataFrame(df)
print(df)

# extracting the top 5 categories
n = df.head()
print(n)

# STEP 9

# VISUALISATION 1
# plotting the number of unique users w.r.t. CID 
y_pos = np.arange(len(n['CID']))
plt.bar(y_pos,n['UUID'])
plt.xticks(y_pos, n['CID'],fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('CID',fontsize=10)
plt.ylabel('No. of unique UUIDs',fontsize=10)
plt.title('Top 5 Categories',fontsize=20)
plt.show()

# VISUALISATION 2
# plotting number of users for each channel
impression['CH'].value_counts().plot.bar(title="Freq dist of Channel Type")
plt.xlabel('Channel',fontsize=10)
plt.ylabel('No. of users',fontsize=10)

# VISUALISATION 3
# getting the correlation matrix 
f, ax = plt.subplots(figsize=(6, 6))
corr = impression.drop(['AdvPixelId','AccountID'],axis=1).corr()
sns.heatmap(corr, xticklabels=corr.columns.values, yticklabels=corr.columns.values,cmap='gist_heat')
