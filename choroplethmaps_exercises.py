import chart_studio.plotly as iplot
import chart_studio.plotly as py
import plotly.graph_objs as go 
import plotly.offline as pyo
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True) 
import pandas as pd

# ** Import pandas and read the csv file: 2014_World_Power_Consumption**

df=pd.read_csv("datasets\\2014_World_Power_Consumption")

# ** Check the head of the DataFrame. **

# print(df.head())

# ** Referencing the lecture notes, create a Choropleth Plot of the Power Consumption for Countries using the data and layout dictionary. **

data = dict(
        type = 'choropleth',
        colorscale = 'Viridis',
        reversescale = True,
        locations = df['Country'],
        locationmode = "country names",
        z = df['Power Consumption KWH'],
        text = df['Country'],
        colorbar = {'title' : 'Power Consumption KWH'},
      ) 

layout = dict(title = '2014 Power Consumption KWH',
                geo = dict(showframe = False,projection = {'type':'mercator'})
             )

# choromap = go.Figure(data = [data],layout = layout)
# pyo.plot(choromap,validate=False)

# ** Import the 2012_Election_Data csv file using pandas. **

df=pd.read_csv("datasets\\2012_Election_Data")

# ** Check the head of the DataFrame. **

# print(df.head())

# ** Now create a plot that displays the Voting-Age Population (VAP) per state. If you later want to play around with other columns, make sure you consider their data type. VAP has already been transformed to a float for you. **

data = dict(type='choropleth',
            colorscale = 'Viridis',
            reversescale = True,
            locations = df['State Abv'],
            z = df['Voting-Age Population (VAP)'],
            locationmode = 'USA-states',
            text = df['State'],
            marker = dict(line = dict(color = 'rgb(255,255,255)',width = 1)),
            colorbar = {'title':"Voting-Age Population (VAP)"}
            )  

layout = dict(title = '2012 General Election Voting Data',
              geo = dict(scope='usa',
                         showlakes = True,
                         lakecolor = 'rgb(85,173,240)')
             )

# choromap = go.Figure(data = [data],layout = layout)
# pyo.plot(choromap,validate=False)