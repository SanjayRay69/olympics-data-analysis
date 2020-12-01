# --------------
import pandas as pd
import numpy as np
# Data Loading
data = pd.read_csv(path)
data.rename(columns = {'Total' : 'Total_Medals'}, inplace = True)
data.head(10)
# Summer or Winter
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', np.where(data['Total_Summer'] < data['Total_Winter'], 'Winter', 'Both'))
better_event = data['Better_Event'].value_counts().idxmax()
print(better_event)
# Top 10
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']].copy()
top_countries = top_countries.iloc[: -1]
def top_ten(top_countries, col_name):
    country_list = []
    x = top_countries.nlargest(10, col_name)
    country_list.append(x)
    return country_list
top_10_summer = list(top_ten(top_countries, 'Total_Summer')[0]['Country_Name'])
top_10_winter = list(top_ten(top_countries, 'Total_Winter')[0]['Country_Name'])
top_10 = list(top_ten(top_countries, 'Total_Medals')[0]['Country_Name'])
common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
# Plotting Top 10
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
import matplotlib.pyplot as plt 
summer_df.plot(x='Country_Name', y='Total_Medals', kind='bar')
plt.ylabel("Total Medals Won")
plt.xlabel("Country")
plt.show()
winter_df.plot(x='Country_Name', y='Total_Medals', kind='bar')
plt.ylabel("Total Medals Won")
plt.xlabel("Country")
plt.show()
top_df.plot(x='Country_Name', y='Total_Medals', kind='bar')
plt.ylabel("Total Medals Won")
plt.xlabel("Country")
plt.show()
# Top performing country(Gold)
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df[summer_df['Golden_Ratio'] == summer_max_ratio]['Country_Name']
winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df[winter_df['Golden_Ratio'] == winter_max_ratio]['Country_Name']
top_df['Golden_Ratio'] = top_df['Gold_Total']/summer_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df[top_df['Golden_Ratio'] == top_max_ratio]['Country_Name'].values[0]
# Best in the world
data_1 = data.iloc[: -1]
data_1['Total_Points'] = data_1['Gold_Total']*3  + data_1['Silver_Total']*2 + data_1['Bronze_Total']*1
most_points = data_1['Total_Points'].max()
best_country = data_1[data_1['Total_Points'] == most_points]['Country_Name'].values[0]
best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
# Plot for the best
ax = best.plot.bar(stacked=True)
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation = 45)


