data = {'area':[800,1000,800,1400,1600,1200],
        'age':[20,25,21,26,35,32],
        'income':[100000, 250000,75000, 200000,400000,300000],
        'raint':[2200,6000,1800,7000,10000,8000]
        }

import pandas as pd
from sklearn.linear_model import LinearRegression
# from sklearn.linear_model import train_test_split
df = pd.DataFrame(data)

X = df.drop('raint',axis=1)
# print(X)
y = df['raint']

model = LinearRegression()
model.fit(X, y)
area = 700
age = 27
income = 350000

new_data = pd.DataFrame(
    [[area, age, income]],
    columns=['area', 'age', 'income']
)

x2 = [[700,27,350000]]
print(new_data)
# pred_raint = model.predict([[area,age,income]])

pred_rent = model.predict(x2)
print(pred_rent)
# print(type(pred_raint))

pred_raint = model.predict(new_data)
print(pred_raint[0])