import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
    
# read dataset
df = pd.read_excel('beras_clean.xlsx', 
        usecols=['pixel', 'volume', 'jarak'])

# delete outlier
# df.drop(1, inplace=True)

# Modeling ML

#variabel x dan y.
x = df.drop(columns='volume')
y = df['volume']

#split data menjadi training and testing dengan porsi 80 : 20.
x_train, x_test, y_train, y_test = train_test_split(
                                        x, y, 
                                        train_size=0.8, test_size=0.2, 
                                        random_state=4)

#object linear regresi.
lin_reg = LinearRegression()

#train the model menggunakan training data yang sudah displit.
lin_reg.fit(x_train.values, y_train.values)

def predict(jarak, pixel):
        return lin_reg.predict([[jarak, pixel]])