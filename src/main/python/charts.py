import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib
matplotlib.use('agg')
import seaborn as sb
from tkinter import *
# source /home/yniu/sandbox/mis500_m1/build/venv/bin/activate
#(mis500_m1)[yniu@yniu-edr-dev6 mis500_m1]$ pip install Seaborn
import tkinter
# matplotlib inline
rcParams['figure.figsize'] = 5, 4
sb.set_style("whitegrid")

x = range(1,10)
y = [1,2,3,4,0,4,3,2,1]
plt.plot(x,y)