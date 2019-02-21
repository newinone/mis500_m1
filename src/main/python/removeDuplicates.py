from pandas import DataFrame

DF_obj = DataFrame({
    'column 1': [1, 1, 2, 2, 3, 3, 3],
    'column 2': ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
    'column 3': ['A', 'A', 'B', 'B', 'C', 'C', 'C']
})

# Show duplicate True/False
print(DF_obj.duplicated())

# Drop duplicate
DF_drop = DF_obj.drop_duplicates()
print(DF_drop)

DF_obj = DataFrame({
    'column 1': [1, 1, 2, 2, 3, 3, 3],
    'column 2': ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
    'column 3': ['A', 'A', 'B', 'B', 'C', 'D', 'C']
})

# Drop duplicate row based on column. Row 1, 3 and 6 dropped.
DF_drop = DF_obj.drop_duplicates()
print(DF_drop)


