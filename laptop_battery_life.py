import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

laptop_df = pd.read_csv('laptop_batter_life.csv', names=['charge_time', 'discharge_time'])
laptop_df = laptop_df[laptop_df.charge_time < 4.0]
y = pd.Series(laptop_df['discharge_time'])
X = pd.DataFrame(laptop_df['charge_time'])


X_test = round(float(input()), 2)

print(8.0) if X_test>8.0 else print(X_test*2)

