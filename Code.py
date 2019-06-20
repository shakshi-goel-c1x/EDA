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

# VISUALISATION 4
# selecting seen and ts column from pixel_shopclues log to find how many new users have been discovered
d = pixel_shopclues[['seen', 'ts']]
print(d)
d = pd.DataFrame(d)
#Converting unix time stamp into readable date.
from datetime import datetime
y = pixel_shopclues.iloc[:,22]
y = list(y)
for i in range(len(y)):
    y[i] /=1000
    # if you encounter a "year is out of range" error the timestamp    # may be in milliseconds, try `ts /= 1000` in that case
    y[i] = datetime.utcfromtimestamp(y[i]).strftime('%Y-%m-%d %H:%M:%S')
print(y)
#Counting number of users discovered between a timestamp
tsb = input("Enter the start date in yyyy-mm-dd hh:mm:ss")
tse = input("Enter the end date in yyyy-mm-dd hh:mm:ss")
X = pixel_shopclues.iloc[:,20]
X = list(X)
t=0
f=0
for i in range(len(X)):
    if((int(y[i][:4]) <= int(tse[:4])) and (int(y[i][5:7]) <= int(tse[5:7])) and (int(y[i][8:10]) <= int(tse[8:10])) and (int(y[i][11:13]) <= int(tse[11:13])) and (int(y[i][14:16]) <= int(tse[14:16])) and (int(y[i][17:19]) <= int(tse[17:19]))):
        if(X[i]==True):
            t+=1
        else:
            f+=1
print("Number of new users is between {} and {} is {}" .format(tsb,tse,f))
#Visualising
x = np.arange(2)
usersDiscovered = [t,f]
fig, ax = plt.subplots()
plt.bar(x, money)
plt.xticks(x, ('Old Users', 'New Users'))
plt.title('Users from {} to {}'.format(tsb,tse))
plt.show()

# VISUALISATION 5
df = capacity[['CID','Na','Ns']]
df = pd.DataFrame(df)
x=0
te=[]
vacant=[]
complete = []
for index,row in df.iterrows():
    for j in row:
        if not(x==0):
            te.append(j)
        else:
            c = j
        x+=1
    x=0 
   diff = te[1]-te[0]
    if(diff!=0):
        te.append(c)
        vacant.append(te)
    else:        te.append(c)
        complete.append(te)
    te=[]
print(len(vacant),len(complete))
# Visualising
x = np.arange(2)
servedVsAvailable = [len(vacant),len(complete)]
fig, ax = plt.subplots()
plt.bar(x,servedVsAvailable)
plt.xticks(x, ('Served Completely', 'Not Served Completely'))
plt.title('Number of Categories which served Native ADs in all the slots available to it')
plt.show()
