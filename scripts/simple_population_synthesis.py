from copy import deepcopy

import pandas
from numpy import sum

# Marginal control distribution
census_income = pandas.read_csv("data/population/census_income.csv", sep=";")
census_occupation = pandas.read_csv("data/population/census_occupation.csv", sep=";")

# household travel survey
hts = pandas.read_csv("data/population/hts.csv", sep=";")

# total iterations
total_iterations = 50

# -------------------------------
# code starts
# -------------------------------
hts = hts.set_index("occupation")
census_occupation = census_occupation.set_index("occupation")
census_income = census_income.set_index("income")

ori_hts = deepcopy(hts)

iter = 0
while iter <= total_iterations:
    # update rows
    for i in range(len(hts.index)):
        cur_occupation_index = hts.index[i] # e.g., teacher, doctor etc.
        original_total_row = sum(hts.iloc[i].values)
        target_total_row = census_occupation.loc[cur_occupation_index].values[0]
        cur_factor = target_total_row / original_total_row

        hts.loc[cur_occupation_index] *= cur_factor

    # update columns
    for i in range(len(hts.columns)):
        cur_income_index = hts[hts.columns[i]] # e.g., 500, 1000, etc.
        original_total_columns = sum(hts[hts.columns[i]] )
        target_total_columns = census_income.loc[int(hts.columns[i])].values[0]
        cur_factor = target_total_columns / original_total_columns

        hts[hts.columns[i]] *= cur_factor
    
    iter += 1

print("population synthesis")
print(hts)

print("population sample")
print(ori_hts)



