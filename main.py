import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.metrics import mean_squared_error, accuracy_score, explained_variance_score

if __name__ == "__main__":
    def train(x, y):
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.33)
        print('x test:', x_test)
        print('y test:', y_test)

        a, b = np.polyfit(x_test, y_test, 1)
        fitLine = a * x_test + b

        plt.xlabel('Age')
        plt.ylabel('Blood Sugar Level (GLU)')
        plt.scatter(x_test, y_test, color='purple')
        plt.plot(x_test, fitLine, color='black')
        plt.suptitle('Diabetes Graph')
        plt.show()

        new_model = input('Would you like a new model? (Y/N)')
        print(new_model)
        if new_model == "Y":
            train(x, y)
        else:
            search(a, b)


    def search(a, b):
        user_data = input('What X Value would you like to search with?')

        answer = float(user_data)*a+b
        print(answer, 'is your y-value based on the test data.')
        searchagain = input('Would you like to search again? (Y/N)')
        if searchagain == 'Y':
            search(a, b)
        else:
            graphagain = input('Would you like a new graph? (Y/N)')
            if graphagain == "Y":
                train(x, y)
            else:
                pass

    ddata = load_diabetes()
    #x, y = load_diabetes(return_X_y=True)
    df_diabetes = pd.DataFrame(data=ddata.data)
    #print(df_diabetes.head())
    #print(df_diabetes.shape)
    #print(df_diabetes.columns)
    x = df_diabetes[0]
    #print(x)
    y = df_diabetes[9]
    #print(y)
    train(x, y)


