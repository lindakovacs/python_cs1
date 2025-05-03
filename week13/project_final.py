#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 14:42:33 2025

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

# Calculate the correlation coefficient between confirmed cases and deaths
correlation_coefficient = np.corrcoef(confirmed_cases, deaths)[0, 1]
print(f"Correlation Coefficient between Confirmed Cases and Deaths: {correlation_coefficient:.2f}")

# Scatter plot of Confirmed Cases vs Deaths
plt.figure(figsize=(10, 6))
plt.scatter(confirmed_cases, deaths, color='purple', alpha=0.6, edgecolor='k')
plt.title('Scatter Plot of Confirmed Cases vs Deaths')
plt.xlabel('Confirmed Cases')
plt.ylabel('Deaths')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

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

# Group data by state and sum confirmed cases
statewise_confirmed = data.groupby('Province_State')['Confirmed'].sum()

# Get the top 10 states by confirmed cases
top_10_states = statewise_confirmed.sort_values(ascending=False).head(10)

# Plot the top 10 states
plt.figure(figsize=(12, 6))
top_10_states.plot(kind='bar', color='blue', alpha=0.7)
plt.title('Top 10 States by Confirmed Cases')
plt.xlabel('State')
plt.ylabel('Confirmed Cases')
plt.xticks(rotation=45)
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
covid_map.save('/Users/lindakovacs/Documents/Python/week13/covid_map.html')
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

# Calculate daily growth rate
data['Daily_Growth_Confirmed'] = data['Daily_Confirmed'] / data['Confirmed'].shift(1) * 100
data['Daily_Growth_Deaths'] = data['Daily_Deaths'] / data['Deaths'].shift(1) * 100

# Plot daily growth rate
plt.figure(figsize=(12, 6))
plt.plot(last_update, data['Daily_Growth_Confirmed'], label='Daily Growth Rate (Confirmed Cases)', color='orange', marker='o', markersize=3)
plt.plot(last_update, data['Daily_Growth_Deaths'], label='Daily Growth Rate (Deaths)', color='purple', marker='x', markersize=3)
plt.xlabel('Date')
plt.ylabel('Growth Rate (%)')
plt.title('Daily Growth Rate of COVID-19 Confirmed Cases and Deaths')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Calculate mortality rate
data['Mortality_Rate'] = (data['Deaths'] / data['Confirmed']) * 100

# Plot mortality rate over time
plt.figure(figsize=(12, 6))
plt.plot(last_update, data['Mortality_Rate'], label='Mortality Rate (%)', color='red', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Mortality Rate (%)')
plt.title('COVID-19 Mortality Rate Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot recovery rate and mortality rate over time
plt.figure(figsize=(12, 6))
plt.plot(last_update, recovery_rate, label='Recovery Rate (%)', color='green', linestyle='--')
plt.plot(last_update, data['Mortality_Rate'], label='Mortality Rate (%)', color='red', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Percentage')
plt.title('COVID-19 Recovery Rate vs Mortality Rate Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Print average mortality rate
avg_mortality_rate = np.mean(data['Mortality_Rate'])
print(f"Average Mortality Rate: {avg_mortality_rate:.2f}%")

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

# Prepare data for mortality rate prediction
X_mortality = np.arange(len(data)).reshape(-1, 1)  # Days as independent variable
y_mortality = data['Mortality_Rate'].fillna(0)  # Mortality rate as dependent variable

# Train the model
model_mortality = LinearRegression()
model_mortality.fit(X_mortality, y_mortality)

# Predict future mortality rates
future_mortality = model_mortality.predict(np.arange(len(data) + 30).reshape(-1, 1))

# Plot predictions
plt.figure(figsize=(12, 6))
plt.plot(last_update, data['Mortality_Rate'], label='Actual Mortality Rate', color='red')
plt.plot(np.arange(len(data) + 30), future_mortality, label='Predicted Mortality Rate', color='orange', linestyle='--')
plt.xlabel('Days')
plt.ylabel('Mortality Rate (%)')
plt.title('COVID-19 Mortality Rate Prediction')
plt.legend()
plt.tight_layout()
plt.show()

# Print latitude, longitude, and confirmed cases
print(data[['Lat', 'Long_', 'Confirmed']].head())
