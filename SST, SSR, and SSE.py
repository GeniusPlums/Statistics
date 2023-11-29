import numpy as np
import statsmodels.api as sm

np.random.seed(1)
x = np.random.randn(100)
X = np.column_stack([x, x**2])

X = sm.add_constant(X)

y = 2*x + 3*x**2 + np.random.randn(100)

model = sm.OLS(y, X).fit()

y_predicted = model.predict(X)

ssr = np.sum((y_predicted - y.mean())**2)  
sse = np.sum((y - y_predicted)**2)
sst = ssr + sse

print(f'SSR: {ssr:.2f}, SSE: {sse:.2f}, SST: {sst:.2f}')