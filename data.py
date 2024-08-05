import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

cpi = pd.read_excel("cpi.xlsx")
elderly_population = pd.read_excel("elderly_population.xlsx")
welfare_budget = pd.read_excel("welfare_budget.xlsx")

base_year = 2007
base_cpi = cpi.loc[cpi['Year'] == base_year, 'CPI'].values[0]
base_population = elderly_population.loc[elderly_population['Year'] == base_year, 'Population'].values[0]
base_budget = welfare_budget.loc[welfare_budget['Year'] == base_year, 'Budget'].values[0]

welfare_budget.insert(2,'CPI',cpi['CPI'])

welfare_budget['Real_Budget'] = welfare_budget.apply(lambda row: (row['Budget'] / row['CPI']) * base_cpi, axis=1)
cpi['CPI_Indexed'] = (cpi['CPI'] / base_cpi) * 100
elderly_population['Population_Indexed'] = (elderly_population['Population'] / base_population) 
welfare_budget['Real_Budget_Indexed'] = (welfare_budget['Real_Budget'] / base_budget) 
print(welfare_budget)


plt.figure(figsize=(12, 8))
plt.plot(elderly_population['Year'], elderly_population['Population_Indexed'],marker ='o', label='Indexed Senior Population')
plt.plot(welfare_budget['Year'], welfare_budget['Real_Budget_Indexed'],marker ='o', label='Indexed Real Budget')

for i in range(len(elderly_population)):
    plt.text(elderly_population['Year'][i], elderly_population['Population_Indexed'][i], f"{elderly_population['Population_Indexed'][i]:.1f}", ha='right', va='bottom')

for i in range(len(welfare_budget)):
    plt.text(welfare_budget['Year'][i], welfare_budget['Real_Budget_Indexed'][i], f"{welfare_budget['Real_Budget_Indexed'][i]:.1f}", ha='left', va='bottom')

plt.xlabel('Year')
plt.ylabel('Indexed Value (2007=100)%')

plt.xticks(np.arange(2007,2023,1))
plt.yticks(np.arange(0,200,10))
plt.title('Indexed Senior Population and Real Budget (2007=100)')
plt.legend()
plt.grid(True)
plt.show()
