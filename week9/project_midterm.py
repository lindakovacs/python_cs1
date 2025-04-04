#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 00:05:59 2025

@author: lindakovacs
"""
# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import folium
from sklearn.linear_model import LinearRegression

# Load the dataset
try:
    data = pd.read_csv('covid-19-dataset-1.csv')
except FileNotFoundError:
    print("Error: The file 'covid-19-dataset-1.csv' was not found. Check the file path.")
    exit()

# Drop rows with missing latitude, longitude, or confirmed cases
data = data.dropna(subset=['Lat', 'Long_', 'Confirmed'])

# Select relevant columns
try:
    confirmed_cases = pd.to_numeric(data['Confirmed'], errors='coerce').dropna()
    deaths = pd.to_numeric(data['Deaths'], errors='coerce').dropna()
    recovered = pd.to_numeric(data['Recovered'], errors='coerce').fillna(0)
    last_update = pd.to_datetime(data['Last_Update'], errors='coerce').dropna()
except KeyError as e:
    print(f"Error: Missing required column {e} in the dataset.")
    exit()

# Calculate recovery rate and active cases
recovery_rate = (recovered / confirmed_cases) * 100
active_cases = confirmed_cases - (deaths + recovered)

# Perform calculations
avg_confirmed = np.mean(confirmed_cases)
avg_deaths = np.mean(deaths)
avg_recovery_rate = np.mean(recovery_rate)

mode_confirmed = stats.mode(confirmed_cases, keepdims=False)[0]
mode_deaths = stats.mode(deaths, keepdims=False)[0]

max_confirmed = np.max(confirmed_cases)
min_confirmed = np.min(confirmed_cases)

max_deaths = np.max(deaths)
min_deaths = np.min(deaths)

# Print results
print(f"Average Confirmed Cases: {avg_confirmed}")
print(f"Mode of Confirmed Cases: {mode_confirmed}")
print(f"Max Confirmed Cases: {max_confirmed}")
print(f"Min Confirmed Cases: {min_confirmed}")
print(f"Average Deaths: {avg_deaths}")
print(f"Mode of Deaths: {mode_deaths}")
print(f"Max Deaths: {max_deaths}")
print(f"Min Deaths: {min_deaths}")
print(f"Average Recovery Rate: {avg_recovery_rate:.2f}%")

# Plot confirmed cases, deaths, and recovery rates
plt.figure(figsize=(12, 6))
plt.plot(last_update, confirmed_cases, label='Confirmed Cases', color='blue', marker='o', markersize=3)
plt.plot(last_update, deaths, label='Deaths', color='red', marker='x', markersize=3)
plt.plot(last_update, recovery_rate, label='Recovery Rate (%)', color='green', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Count / Percentage')
plt.title('COVID-19 Confirmed Cases, Deaths, and Recovery Rates Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Group data by state and plot a bar chart
statewise_data = data.groupby('Province_State').sum()
statewise_data[['Confirmed', 'Deaths', 'Recovered']].plot(kind='bar', figsize=(15, 8))
plt.title('Statewise COVID-19 Cases')
plt.xlabel('State')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Create an interactive map
covid_map = folium.Map(location=[37.0902, -95.7129], zoom_start=4)  # Centered on the US
for _, row in data.iterrows():
    folium.CircleMarker(
        location=[row['Lat'], row['Long_']],
        radius=row['Confirmed'] / 1000,  # Scale radius by confirmed cases
        color='red',
        fill=True,
        fill_color='red',
        fill_opacity=0.6,
        popup=f"{row['Admin2']}, {row['Province_State']}: {row['Confirmed']} cases",
    ).add_to(covid_map)

# Save the map
covid_map.save('/Users/lindakovacs/Documents/Python/week9_midterm_project/covid_map.html')
print("Interactive map saved as 'covid_map.html'. Open it in a browser to view.")

# Calculate daily changes
data['Daily_Confirmed'] = data['Confirmed'].diff().fillna(0)
data['Daily_Deaths'] = data['Deaths'].diff().fillna(0)

# Plot daily changes
plt.figure(figsize=(12, 6))
plt.plot(last_update, data['Daily_Confirmed'], label='Daily Confirmed Cases', color='orange', marker='o', markersize=3)
plt.plot(last_update, data['Daily_Deaths'], label='Daily Deaths', color='purple', marker='x', markersize=3)
plt.xlabel('Date')
plt.ylabel('Daily Count')
plt.title('Daily Changes in COVID-19 Confirmed Cases and Deaths')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Prepare data for prediction
X = np.arange(len(data)).reshape(-1, 1)  # Days as independent variable
y = data['Confirmed']  # Confirmed cases as dependent variable

# Train the model
model = LinearRegression()
model.fit(X, y)

# Predict future cases
future_days = np.arange(len(data) + 30).reshape(-1, 1)  # Predict for 30 days ahead
predicted_cases = model.predict(future_days)

# Plot predictions
plt.figure(figsize=(12, 6))
plt.plot(data['Last_Update'], data['Confirmed'], label='Actual Cases', color='blue')
plt.plot(future_days, predicted_cases, label='Predicted Cases', color='orange', linestyle='--')
plt.xlabel('Days')
plt.ylabel('Confirmed Cases')
plt.title('COVID-19 Confirmed Cases Prediction')
plt.legend()
plt.show()

# Print latitude, longitude, and confirmed cases
print(data[['Lat', 'Long_', 'Confirmed']].head())
