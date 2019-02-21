import numpy as np
from pandas import DataFrame, Series

series_obj = Series(
    np.arange(8),
    index=[
        'row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6', 'row 7', 'row 8'
    ])
print(series_obj['row 2'])
print(series_obj[1])

missing = np.nan

series_obj = Series(
    ['row 1', 'row 2', missing, 'row 4', 'row 5', missing, 'row 7', 'row 8'])
print(series_obj)
# list of missing values True/False
print(series_obj.isnull())

np.random.seed(25)
# Generate 6x6 matrix
DF_obj = DataFrame(np.random.randn(36).reshape(6, 6))
print(DF_obj)

# Change some value to missing
DF_obj.ix[3:5, 0] = missing
DF_obj.ix[1:4, 5] = missing
print(DF_obj)

# Fill 0 to missing values
filled_DF = DF_obj.fillna(0)
print(filled_DF)

# Fill column 0 with 0.1 and column 5 with 1.25
filled_DF = DF_obj.fillna({0: 0.1, 5: 1.25})
print(filled_DF)

# Forward fill(copy privious value to NaN)
filled_DF = DF_obj.fillna(method='ffill')
print(filled_DF)


# Count missing values by column
print(DF_obj.isnull().sum())


# Drop all rows with any NaN
DF_no_NaN = DF_obj.dropna()
print(DF_no_NaN)

# Drop all column with any NaN
DF_no_NaN = DF_obj.dropna(axis=1)
print(DF_no_NaN)

# Drop all rows with all values are NaN
DF_no_NaN = DF_obj.dropna(how='all')
print(DF_no_NaN)


