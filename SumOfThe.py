def SumOfThe(N, data):
	for i in range(N):
		x = 0
		result = data[i]
		for j in range(N):
			if j != i:
				x += data[j]
		if x == result:
			return result
