#!/usr/bin/env python
# coding: utf-8

# In Class Assignment #6: build 3 new visualizations using the "workout_data.csv" dataset in Plotly or Plotly Express

# In[1]:
# # import pandas
import pandas as pd

# In[2]:
# # bring in the "workout data" dataset
df = pd.read_csv("/Users/duhlenuh/Downloads/info450/workout_data.csv")

# In[3]:
df

# In[4]:
# # no scatter plots, histograms, box plots, or heatmaps
import plotly.express as px

# In[5]:
# # density contours: shows relationship between duration and calories
fig = px.density_contour(df, x="Duration", y="Calories")
fig.show()

# In[6]:
# # 3d scatter plot: shows relationship between duration, pulse, and maxpulse
fig = px.scatter_3d(df, x = "Duration", y = "Pulse", z = "Maxpulse", color = "Duration")
fig.show()

# In[7]:
# # hover labels
fig = px.scatter(df.query("Duration==60"), x = "Calories", y = "Pulse", size = "Maxpulse", color = "Calories")
fig.show()

# In[8]:
# # empirical cumulative distribution function (ecdf) charts: shows the relationship between duration and pulse
fig = px.ecdf(df, x = "Duration", color = "Pulse")
fig.show()

# In[9]:
fig = px.ecdf(df, x = "Pulse", color = "Duration")
fig.show()

# In[10]:
# # ternary charts
fig = px.scatter_ternary(df, a = "Maxpulse", b = "Pulse", c = "Calories", color = "Duration")
fig.show()