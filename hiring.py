import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from word2number import w2n
from sklearn import linear_model
import math

df = pd.read_csv('hiring.csv')
# print(df)

meantestScore = math.floor(df['test_score(out of 10)'].mean())
# print(median_testScore)

df['test_score(out of 10)'] = df['test_score(out of 10)'].fillna(meantestScore)
df.experience=df.experience.fillna("zero")

# print(df.test_score)
df['experience'] = df['experience'].apply(w2n.word_to_num)
# print(df)
model = linear_model.LinearRegression()
model.fit(df[['experience','test_score(out of 10)','interview_score(out of 10)']],df['salary($)'])

# print(model.predict([[2,9,6]]))
print(model.predict([[12,10,10]]))