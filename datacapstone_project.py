# 911 Calls Capstone Project

# ** Import numpy and pandas **

import pandas as pd
import numpy as np

# ** Import visualization libraries and set %matplotlib inline. **

import matplotlib.pyplot as plt
import seaborn as sns


# ** Read in the csv file as a dataframe called df **

df=pd.read_csv("datasets\\911.csv")

# ** Check the info() of the df **

dat=df.info()

# ** Check the head of df **

dat=df.head()

# ** What are the top 5 zipcodes for 911 calls? **

dat=df["zip"].value_counts().head()

# ** What are the top 5 townships (twp) for 911 calls? **

dat=df["twp"].value_counts().head()

# ** Take a look at the 'title' column, how many unique title codes are there? **

dat=df["title"].nunique()

## Creating new features

# ** In the titles column there are "Reasons/Departments" specified before the title code. These are EMS, Fire, and Traffic. Use .apply() with a custom lambda expression to create a new column called "Reason" that contains this string value.** 

# **For example, if the title column value is EMS: BACK PAINS/INJURY , the Reason column value would be EMS. **

new_index=df["title"].apply(lambda title:title.split(":")[0])
df["reason"]=new_index

# ** What is the most common Reason for a 911 call based off of this new column? **

dat=df["reason"].value_counts()

# ** Now use seaborn to create a countplot of 911 calls by Reason. **

sns.set_style('whitegrid')
sns.countplot(x="reason",data=df)
# plt.show()

# ** Now let us begin to focus on time information. What is the data type of the objects in the timeStamp column? **

dat=type(df["timeStamp"].iloc[0])

# ** You should have seen that these timestamps are still strings. Use [pd.to_datetime](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html) to convert the column from strings to DateTime objects. **

dat=df['timeStamp'] = pd.to_datetime(df['timeStamp'])

# ** You can now grab specific attributes from a Datetime object by calling them. For example:**

#     time = df['timeStamp'].iloc[0]
#     time.hour

# **You can use Jupyter's tab method to explore the various attributes you can call. Now that the timestamp column are actually DateTime objects, use .apply() to create 3 new columns called Hour, Month, and Day of Week. You will create these columns based off of the timeStamp column, reference the solutions if you get stuck on this step.**

# ** Notice how the Day of Week is an integer 0-6. Use the .map() with this dictionary to map the actual string names to the day of the week: **

#     dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}

new_index=df["timeStamp"].apply(lambda timeStamp:timeStamp.hour)
df["hour"]=new_index

new_index=df["timeStamp"].apply(lambda timeStamp:timeStamp.month)
df["month"]=new_index

new_index=df["timeStamp"].apply(lambda timeStamp:(timeStamp.day%7))
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
new_index_mapped=new_index.map(dmap)
df["day of week"]=new_index_mapped
# or
"""
df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)
"""
# ** Now use seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column. **

sns.countplot(x="day of week",data=df,hue="reason")
# To relocate the legend
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# plt.show()

# **Now do the same for Month:**

sns.countplot(x="month",data=df,hue="reason")
# plt.show()

# **Did you notice something strange about the Plot?**

# ** You should have noticed it was missing some Months, let's see if we can maybe fill in this information by plotting the information in another way, possibly a simple line plot that fills in the missing months, in order to do this, we'll need to do some work with pandas... **

# ** Now create a gropuby object called byMonth, where you group the DataFrame by the month column and use the count() method for aggregation. Use the head() method on this returned DataFrame. **

byMonth=df.groupby("month").count()

# ** Now create a simple plot off of the dataframe indicating the count of calls per month. **

byMonth["twp"].plot()
# or
plt.plot(byMonth["twp"])
# plt.show()

# ** Now see if you can use seaborn's lmplot() to create a linear fit on the number of calls per month. Keep in mind you may need to reset the index to a column. **

sns.lmplot(x='month',y='twp',data=byMonth.reset_index())
plt.show()

# **Create a new column called 'Date' that contains the date from the timeStamp column. You'll need to use apply along with the .date() method. ** 

df["date"]=df["timeStamp"].apply(lambda time:time.date())

# ** Now groupby this Date column with the count() aggregate and create a plot of counts of 911 calls.**

byDate=df.groupby("date").count()
plt.plot(byDate["twp"])
plt.tight_layout()
# plt.show()
# or
df.groupby('Date').count()['twp'].plot()
plt.tight_layout()
# plt.show()

# ** Now recreate this plot but create 3 separate plots with each plot representing a Reason for the 911 call**

df[df['reason']=='Traffic'].groupby('date').count()['twp'].plot()
plt.title('EMS')
plt.tight_layout()
# plt.show()

df[df['reason']=='Fire'].groupby('date').count()['twp'].plot()
plt.title('EMS')
plt.tight_layout()
# plt.show()

df[df['reason']=='EMS'].groupby('date').count()['twp'].plot()
plt.title('EMS')
plt.tight_layout()
# plt.show()
# or
"""
df=df[df["reason"]=="EMS"]
byDate=df.groupby("date").count()
plt.plot(byDate["twp"])
plt.tight_layout()
# plt.show()
"""

# ** Now let's move on to creating  heatmaps with seaborn and our data. We'll first need to restructure the dataframe so that the columns become the Hours and the Index becomes the Day of the Week. There are lots of ways to do this, but I would recommend trying to combine groupby with an [unstack](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.unstack.html) method. Reference the solutions if you get stuck on this!**

dayHour = df.groupby(['day of week','hour']).count()['reason'].unstack()
# print(dayHour.head())

# ** Now create a HeatMap using this new DataFrame. **

sns.heatmap(dayHour)

# ** Now create a clustermap using this DataFrame. **

sns.clustermap(dayHour)

# ** Now repeat these same plots and operations, for a DataFrame that shows the Month as the column. **

dayMonth = df.groupby(['day of week','month']).count()['reason'].unstack()
# print(dayHour.head())
sns.heatmap(dayMonth)
sns.clustermap(dayMonth)




