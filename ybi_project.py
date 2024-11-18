# -*- coding: utf-8 -*-
"""YBI PROJECT.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ipphoBPCsf_OMb60QKMcfqc-IsazS323

#Servo Prediction Using Linear Regression
"""

import numpy as np
import pandas as pd

df=pd.read_csv('https://github.com/YBI-Foundation/Dataset/raw/main/Servo%20Mechanism.csv')

df.head()

df.info()

df.describe()

df.columns

df.shape

df[['Motor']].value_counts()

df[['Screw']].value_counts()

df.replace({'Motor':{'A':0,'B':1,'C':2,'D':3,'E':4}},inplace=True)
df.replace({'Screw':{'A':0,'B':1,'C':2,'D':3,'E':4}},inplace=True)

y=df['Class']

y.shape

y

X=df[['Motor', 'Screw', 'Pgain', 'Vgain']]

X.shape

X

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=2529)

from sklearn.linear_model import LinearRegression

lr=LinearRegression()

lr.fit(X_train,y_train)

y_pred=lr.predict(X_test)

y_pred.shape

y_pred

from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score

mean_squared_error(y_test,y_pred)

r2_score(y_test,y_pred)

mean_absolute_error(y_test,y_pred)

import matplotlib.pyplot as plt
plt.scatter(y_test,y_pred)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Actual Vs Predicted")
plt.show()

X_new=df.sample(1)

X_new

X_new.shape

X_new=X_new.drop('Class',axis=1)

X_new

y_pred_new=lr.predict(X_new)

y_pred_new