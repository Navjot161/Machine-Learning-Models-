import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
import math
import joblib

df = pd.read_csv("houseprice.csv")
# print(df)
bedroomsMedian = math.floor(df.bedrooms.median())

df.bedrooms = df.bedrooms.fillna(bedroomsMedian)
# print(df)
reg = linear_model.LinearRegression()
reg.fit(df[['area','bedrooms','age']],df.price)

joblib.dump(reg, 'model.pkl')
prediction = reg.predict([[3500,3,40]])
print(prediction)