# --------------
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
# code starts here
df = pd.read_csv(path)
print(df.head())
X = df[['ages', 'num_reviews', 'piece_count', 'play_star_rating', 'review_difficulty', 'star_rating', 'theme_name', 'val_star_rating', 'country']]
y = df['list_price']
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.3 , random_state = 6)
# code ends here


# --------------
import matplotlib.pyplot as plt

cols = X_train.columns
rows = 3
columns = 3
fig, axes = plt.subplots(nrows = rows, ncols = columns, figsize=(20, 10))
for i in range(0,rows,1):
    for j in range(0,columns,1):
        col = cols[i*3 + j]
        axes[i, j].scatter(X[col], y)
        plt.ylabel(str.upper('Price'))
        plt.xlabel(str.upper(col))
        plt.xticks(rotation = 45)
plt.show()


# --------------
# Code starts here
corr = X_train.corr()
print(corr)
X_train = X_train.drop(['play_star_rating', 
                        'val_star_rating'], axis=1)
X_test = X_test.drop(['play_star_rating', 
                        'val_star_rating'], axis=1)
# Code ends here


# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Code starts here
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)
print(mse)
print(r2)
# Code ends here


# --------------
# Code starts here
residual = (y_test - y_pred)
plt.figure(figsize=(15,8))
plt.hist(residual, bins=30)
plt.xlabel("Residual Error")
plt.ylabel("Frequency") 
plt.title("Error Residual plot")
plt.show()
# Code ends here


