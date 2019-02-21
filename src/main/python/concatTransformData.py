import numpy as np
import pandas as pd
from pandas import DataFrame, Series

#
DF_obj = pd.DataFrame(np.arange(36).reshape(6, 6))
DF_obj2 = pd.DataFrame(np.arange(15).reshape(5, 3))

# Join by column
DF_col_join = pd.concat([DF_obj, DF_obj2], axis=1)
print(DF_col_join)

# Join by row
DF_row_join = pd.concat([DF_obj, DF_obj2])
print(DF_row_join)

# Drop rows 0 and 2
print(DF_obj.drop([0, 2]))

# Drop column 0 and 2
print(DF_obj.drop([0, 2], axis=1))

series_obj = Series(np.arange(6))
series_obj.name = "added_variable"

print(series_obj)
# Add column to after the last column of the DF
variable_added = DataFrame.join(DF_obj, series_obj)
print(variable_added)

# Not reindex after append row
added_datatable = variable_added.append(variable_added, ignore_index=False)
print(added_datatable)

# reindex row after append row
added_datatable = variable_added.append(variable_added, ignore_index=True)
print(added_datatable)

# Sorting data desc by column 5
print(DF_obj.sort_values(by=[5], ascending=[False]))
