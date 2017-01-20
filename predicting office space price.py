import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


# get the first line with the test data shape
train_shape = input().split()
cols = int(train_shape[0]) + 1
rows = int(train_shape[1])

my_list = list()

y = np.ndarray(rows)
X = list()

for row in range(rows):
    tmp_list = input().split()
    y[row] = tmp_list[cols - 1]
    X.append(tmp_list[0:cols - 1])

X_df = pd.DataFrame(X, columns=['x' + str(i) for i in range(cols - 1)])

test_shape = input().split()
rows = int(test_shape[0])
X_test = list()

for row in range(rows):
    tmp_list = input().split()
    X_test.append(tmp_list[0:cols - 1])

X_test_df = pd.DataFrame(X_test, columns=['x' + str(i) for i in range(cols - 1)])

my_fit = LinearRegression()

my_fit.fit(X_df, y)

my_predict = my_fit.predict(X_test_df)

for i in my_predict:
    print(i)
