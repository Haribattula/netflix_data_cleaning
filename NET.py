#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install matplotlib


# In[5]:


pip install seaborn


# In[6]:


# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


# Load data
data = pd.read_csv("C:/netflix_data_cleaning/netflix_titles.csv")

# Display the first few rows of the dataset
data.head()


# In[8]:


# Inspect data
print(data.info())
print(data.describe())


# In[10]:


# Check for missing values
print(data.isnull().sum())

# Forward fill missing values
data.ffill(inplace=True)

# Alternatively, use backward fill
# data.bfill(inplace=True)

# Or fill with a specific value
# data.fillna(value=0, inplace=True)

# Drop rows with missing values
# data.dropna(inplace=True)

# Verify that there are no missing values left
print(data.isnull().sum())


# In[11]:


# Remove duplicates
data.drop_duplicates(inplace=True)


# In[17]:


# Convert 'date_added' column to datetime with error handling
data['date_added'] = pd.to_datetime(data['date_added'], format='%B %d, %Y', errors='coerce')

# Check for any conversion issues
print(data['date_added'].isnull().sum())


# In[19]:


# List all column names
print("Columns:", data.columns)

# Display the first few rows
print(data.head())

# If column names have extra spaces, strip them
data.columns = data.columns.str.strip()

# Verify column names again
print("Cleaned Columns:", data.columns)

# Convert the 'date_added' column to datetime
data['date_added'] = pd.to_datetime(data['date_added'], format='%B %d, %Y')

# Verify the conversion
print(data['date_added'].head())


# In[20]:


# Convert 'release_year' to integer if it isn't already
data['release_year'] = data['release_year'].astype(int)

# Example: Create a new column for the decade
data['decade'] = (data['release_year'] // 10) * 10


# In[21]:


# Count the number of shows per country
shows_per_country = data['country'].value_counts()

# Display the result
print(shows_per_country)


# In[22]:


import matplotlib.pyplot as plt
import seaborn as sns

# Plot the distribution of shows by country
plt.figure(figsize=(12, 6))
sns.countplot(y='country', data=data, order=data['country'].value_counts().index)
plt.title('Number of Shows by Country')
plt.xlabel('Count')
plt.ylabel('Country')
plt.show()


# In[24]:


import sqlite3

# Step 1: Connect to SQLite Database
# 'netflix_data.db' is the name of the database file
conn = sqlite3.connect('netflix_data.db')

# Step 2: Store the DataFrame in the Database
# The table name is 'netflix_transformed'
data.to_sql('netflix_transformed', conn, if_exists='replace', index=False)

# Step 3: Close the Connection
conn.close()


# In[26]:


# Reconnect to the database
conn = sqlite3.connect('netflix_data.db')

# Read data from the 'netflix_transformed' table into a DataFrame
query = 'SELECT * FROM netflix_transformed'
transformed_data = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Display the first few rows of the transformed data
print(transformed_data.head())


# In[ ]:


## Summary of Findings

- **Top Countries**: The United States has the highest number of shows available on Netflix.
- **Trends Over Time**: There has been a significant increase in the number of shows released over the years.

## Data Transformations

- **Date Conversion**: Converted the `date_added` column to a datetime format.
- **Duration Extraction**: Extracted numerical values from the `duration` column to calculate average duration.

## Visualizations

- Distribution of Shows by Country
- Number of Shows Released per Year


# In[31]:


#Distribution of Shows by Country
import warnings

# Suppress all FutureWarnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Your plotting code
import matplotlib.pyplot as plt
import seaborn as sns

# Plot the distribution of shows by country
plt.figure(figsize=(12, 8))
sns.countplot(y='country', data=data, order=data['country'].value_counts().index, palette='viridis')
plt.title('Number of Shows by Country')
plt.xlabel('Count')
plt.ylabel('Country')
plt.show()


# In[32]:


#Number of Shows Released per Year
# Convert 'release_year' to numeric if it isn't already
data['release_year'] = pd.to_numeric(data['release_year'], errors='coerce')

# Plot trends over time for the number of shows released each year
plt.figure(figsize=(12, 6))
data['release_year'].dropna().astype(int).value_counts().sort_index().plot(kind='line', marker='o')
plt.title('Number of Shows Released per Year')
plt.xlabel('Year')
plt.ylabel('Number of Shows')
plt.grid(True)
plt.show()


# In[ ]:




