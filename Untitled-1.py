# Importing main libraries mm

import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_inline
import seaborn as sns

# Importing data from system, we have our data in CSV form
df=pd.read_csv("C:/Users/hchou/OneDrive/Desktop/Advertising.csv")
df.head()   # Checking head of the data



