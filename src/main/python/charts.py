import numpy as np
import pandas as pd
from pandas import DataFrame, Series

series_obj = Series(
    np.arange(8),
    index=[
        'row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6', 'row 7', 'row 8'
    ])
print(series_obj['row 2'])
print(series_obj[1])
