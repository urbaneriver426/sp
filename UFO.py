def UFO(N, data, octal=True):
	result = []

	if octal == True:
		numSys = 8
	else:
		numSys = 16

	for i in range(N):
		currNum = str(data[i])
		y = 0
		
		for j in range(len(currNum)):
			x = numSys**(len(currNum)-(1+j)) * int(currNum[j])
			y += x
		
		result.append(y)
	return result
