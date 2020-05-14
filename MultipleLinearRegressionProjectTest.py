# Multiple Linear Regression Project Test

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('PS_20174392719_1491204439457_log.csv')

X = dataset.iloc[:, [1,2,4,5,7,8]].values
y = dataset.iloc[:, 9].values

# Encoding categorical data: Transforms string data to binary values
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 0] = labelencoder.fit_transform(X[:, 0])
#need numbers because ONeHotEncoder can't use strings
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling: All values are within similar range
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LogisticRegression #40%-50% 
regressor = LogisticRegression()

regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Visualising the Training set results
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred);





