def printVector(X):
	print(*X)

def rankify(X):

	N = len(X)

	Rank_X = [None for _ in range(N)]

	for i in range(N):

		r = 1
		s = 1

		for j in range(i):
			if (X[j] < X[i]):
				r += 1
			if (X[j] == X[i]):
				s += 1

		for j in range(i+1, N):
			if (X[j] < X[i]):
				r += 1
			if (X[j] == X[i]):
				s += 1

		Rank_X[i] = r + (s-1) * 0.5

	return Rank_X

def correlationCoefficient(X, Y):
	n = len(X)
	sum_X = 0
	sum_Y = 0
	sum_XY = 0
	squareSum_X = 0
	squareSum_Y = 0

	for i in range(n):

		sum_X = sum_X + X[i]

		sum_Y = sum_Y + Y[i]

		sum_XY = sum_XY + X[i] * Y[i]

		squareSum_X = squareSum_X + X[i] * X[i]
		squareSum_Y = squareSum_Y + Y[i] * Y[i]

	corr = (n * sum_XY - sum_X * sum_Y) / ((n * squareSum_X -
											sum_X * sum_X) * (n * squareSum_Y - sum_Y * sum_Y)) ** 0.5

	return corr

X = [14, 10, 12, 17, 10, 15, 10, 12, 19, 11]
Y = [21, 16, 32, 25, 30, 16, 20, 22, 35, 23]

rank_x = rankify(X)

rank_y = rankify(Y)

print("Vector X")
printVector(X)

print("Rankings of X")
printVector(rank_x)

print("Vector Y")
printVector(Y)

print("Rankings of Y")
printVector(rank_y)

print("Spearman's Rank correlation: ")
print(correlationCoefficient(rank_x, rank_y))