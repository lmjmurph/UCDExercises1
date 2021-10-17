import pandas as pd
import numpy as np

# Exercises 1, 2

# Cannot replicate as the categories dataframe is not provided

# Exercise 3
airlines = pd.read_csv("airlines_final.csv")
# Print unique values of both columns
print(airlines.info())
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

# Lower dest_region column and then replace "eur" with "europe"
airlines['dest_region'] = airlines['dest_region'].str.lower()
airlines['dest_region'] = airlines['dest_region'].replace({'eur':'europe'})
