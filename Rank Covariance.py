import numpy as np
from scipy.stats import spearmanr, rankdata

X = np.array([14, 10, 12, 17, 10, 15, 10, 12, 19, 11])
Y = np.array([21, 16, 32, 25, 30, 16, 20, 22, 35, 23])

rank_x = rankdata(X)
rank_y = rankdata(Y)

print(f"Vector X: {X}")
print(f"Rankings of X: {rank_x}")
print(f"Vector Y: {Y}")
print(f"Rankings of Y: {rank_y}")

corr, _ = spearmanr(rank_x, rank_y)
print(f"Spearman's Rank correlation: {corr}")