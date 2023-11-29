import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel('Data_Lecture 3.xlsx')

def estimate_coef(x, y):
    # calculating regression coefficients
    b_1 = np.cov(x, y)[0, 1] / np.var(x)
    b_0 = np.mean(y) - b_1 * np.mean(x)

    return b_0, b_1

def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m", marker = "o", s = 30)

    # predicted response vector
    y_pred = b[0] + b[1]*x

    # plotting the regression line
    plt.plot(x, y_pred, color = "g")

    # putting labels
    plt.xlabel('Ad expenses')
    plt.ylabel('Sales')

    # function to show plot
    plt.show()

def main():
    # read data from excel file
    df = pd.read_excel('Data_Lecture 3.xlsx')

    # observations / data
    x = df[' Advertisement Expenses (in lakhs, Rs.)'].values
    y = df['Sales  (in lakhs, Rs.)'].values

    # estimating coefficients
    b = estimate_coef(x, y)
    print("Estimated coefficients:\nb_0 = {} \
        \nb_1 = {}".format(b[0], b[1]))

    # plotting regression line
    plot_regression_line(x, y, b)

if __name__ == "__main__":
    main()