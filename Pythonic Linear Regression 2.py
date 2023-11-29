import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
    # calculating regression coefficients
    b_1 = np.cov(x, y)[0, 1] / np.var(x)
    b_0 = np.mean(y) - b_1 * np.mean(x)

    return b_0, b_1

def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="m", marker="o", s=30)

    # predicted response vector
    y_pred = b[0] + b[1]*x

    # plotting the regression line
    plt.plot(x, y_pred, color="g")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    # function to show plot
    plt.show()

def main():
    # observations / data
    x = np.array([10, 12, 20, 15, 16, 18, 19, 20, 11, 14, 15, 17, 10, 16, 13])
    y = np.array([24, 25, 30, 28, 25, 30, 32, 35, 20, 26, 28, 35, 22, 32, 24])

    # estimating coefficients
    b = estimate_coef(x, y)
    print(f"Estimated coefficients:\nb_0 = {b[0]}\nb_1 = {b[1]}")

    # plotting regression line
    plot_regression_line(x, y, b)

if __name__ == "__main__":
    main()