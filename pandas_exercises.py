# FİRST EXERCİSES

# ** Import pandas as pd.**

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ** Read Salaries.csv as a dataframe called sal.**

data=pd.read_csv("datasets\\Salaries.csv")

# ** Check the head of the DataFrame. **

salary=data.head()

# ** Use the .info() method to find out how many entries there are.**

"""salary=data.info()"""

# **What is the average BasePay ?**

salary=data["BasePay"].mean()

# ** What is the highest amount of OvertimePay in the dataset ? **

salary=data["OvertimePay"].max()

# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

salary=data[(data['EmployeeName']=="JOSEPH DRISCOLL")]["JobTitle"]

# ** How much does JOSEPH DRISCOLL make (including benefits)? **

salary=data[(data['EmployeeName']=="JOSEPH DRISCOLL")]["TotalPayBenefits"]

# ** What is the name of highest paid person (including benefits)?**

salary=data[data['TotalPayBenefits']== data['TotalPayBenefits'].max()] #['EmployeeName']
# or
# sal.loc[sal['TotalPayBenefits'].idxmax()]

# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

salary=data[data["TotalPayBenefits"]==data["TotalPayBenefits"].min()]
# or
# salary= data.loc[data['TotalPay'].idxmin()]

# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

numeric_data = data.select_dtypes(include='number')
salary = numeric_data.groupby(['Year']).mean()["BasePay"]

# ** How many unique job titles are there? **

# salary=len(data["JobTitle"].unique())
salary=data['JobTitle'].nunique()

# ** What are the top 5 most common jobs? **

salary=data["JobTitle"].value_counts().head()

# ** How many Job Titles were represented by only one perJson in 2013? (e.g. Job Titles with only one occurence in 2013?) **

salary=sum(data[data['Year']==2013]['JobTitle'].value_counts() == 1) 

#**************************

# ** How many people have the word Chief in their job title? (This is pretty tricky) **

def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False

a=sum(data['JobTitle'].apply(lambda x: chief_string(x)))
# print(a)

# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

data['title_len'] = data['JobTitle'].apply(len)

b=data[['title_len','TotalPayBenefits']].corr()
# print(b)

# SECOND EXERCİSES


# ** Import pandas and read in the Ecommerce Purchases csv file and set it to a DataFrame called ecom. **

import pandas as pd
import numpy as np
ecom=pd.read_csv("datasets\\Ecommerce Purchases")

# **Check the head of the DataFrame.**

purch=ecom.head()

# ** How many rows and columns are there? **

"""purch=ecom.info()"""

# ** What is the average Purchase Price? **

purch=ecom["Purchase Price"].mean()

# ** What were the highest and lowest purchase prices? **

purch=ecom['Purchase Price'].max()

purch=ecom['Purchase Price'].min()

# ** How many people have English 'en' as their Language of choice on the website? **

purch=ecom[ecom["Language"]=="en"].count()
# purch=ecom[ecom["Language"]=="en"].info()

# ** How many people have the job title of "Lawyer" ? **
# salary=data[(data['EmployeeName']=="JOSEPH DRISCOLL")]["JobTitle"]


purch=len(ecom[(ecom["Job"]=="Lawyer")]["Job"].index)
purch=ecom[(ecom["Job"]=="Lawyer")]["Job"].count()
# purch=ecom[(ecom["Job"]=="Lawyer")]["Job"].info()

# ** How many people made the purchase during the AM and how many people made the purchase during PM ? **
# **(Hint: Check out [value_counts()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html) ) **

purch=ecom["AM or PM"].value_counts()

# ** What are the 5 most common Job Titles? **

purch=ecom["Job"].value_counts().head()

# ** Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction? **

purch=ecom[(ecom["Lot"]=="90 WT")]["Purchase Price"]

# ** What is the email of the person with the following Credit Card Number: 4926535242672853 **

purch=ecom[(ecom["Credit Card"]==4926535242672853)]["Email"]

# ** How many people have American Express as their Credit Card Provider *and* made a purchase above $95 ?**
# ope = df5[(df5['col1']>2) & (df5['col2']==444)]

purch=ecom[(ecom["CC Provider"]=="American Express") & (ecom["Purchase Price"]>95)].count()
purch=len(ecom[(ecom["CC Provider"]=="American Express") & (ecom["Purchase Price"]>95)].index)

# ** Hard: How many people have a credit card that expires in 2025? **

purch=sum(ecom["CC Exp Date"].apply(lambda exp: exp[3:]=="25"))
purch=ecom[ecom["CC Exp Date"].apply(lambda exp: exp[3:]=="25")].count()
purch=len(ecom[ecom["CC Exp Date"].apply(lambda exp: exp[3:]=="25")].index)

# ** Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...) **

purch=ecom["Email"].apply(lambda email: email.split("@")[1]).value_counts().head()
# print(purch)

# example_email=ecom["Email"].iloc[0]
# example_email=example_email.split("@")
# print(example_email)

# THİRD EXERCİSES 


df3 = pd.read_csv('datasets\\df3')

a=df3.head()

# ** Recreate this scatter plot of b vs a. Note the color and size of the points. Also note the figure size. See if you can figure out how to stretch it in a similar fashion. Remeber back to your matplotlib lecture...**

df3.plot.scatter(x='a',y='b',color="red",figsize=(12,3),s=50)

# ** Create a histogram of the 'a' column.**

df3["a"].plot.hist()
df3['a'].plot(kind="hist")

# ** These plots are okay, but they don't look very polished. Use style sheets to set the style to 'ggplot' and redo the histogram from above. Also figure out how to add more bins to it.***

plt.style.use('ggplot') 
df3['a'].plot(kind="hist",bins=30)

# ** Create a boxplot comparing the a and b columns.**

df3[['a','b']].plot.box()

# ** Create a kde plot of the 'd' column **

df3['d'].plot.kde()

# ** Figure out how to increase the linewidth and make the linestyle dashed. (Note: You would usually not dash a kde plot line)**

df3['d'].plot.density(lw=5,ls='--')

# ** Create an area plot of all the columns for just the rows up to 30. (hint: use .ix).**

df3.iloc[0:30].plot.area(alpha=0.4)

# ## Bonus Challenge!
# Note, you may find this really hard, reference the solutions if you can't figure it out!
# ** Notice how the legend in our previous figure overlapped some of actual diagram. Can you figure out how to display the legend outside of the plot as shown below?**

# ** Try searching Google for a good stackoverflow link on this topic. If you can't find it on your own - [use this one for a hint.](http://stackoverflow.com/questions/23556153/how-to-put-legend-outside-the-plot-with-pandas)**

f = plt.figure()
df3.iloc[0:30].plot.area(alpha=0.4,ax=f.gca())
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))






    