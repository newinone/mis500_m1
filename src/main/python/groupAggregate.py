import numpy as np
import pandas as pd
from pandas import DataFrame, Series


address = '../../../resources/mtcars.csv'

cars = pd.read_csv(address)
cars.columns = ['mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
print(cars.head())

# Group records by cyl and print means of each group
cars_groups = cars.groupby(cars['cyl'])
print(cars_groups.mean())

