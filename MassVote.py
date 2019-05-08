def MassVote(n, votes):
	sumOfVoices = 0
	count = 0

	for i in range(n):
		sumOfVoices += votes[i]
	

	for j in range(n):
		if j == 0:
			winnerPercent = round(votes[j] / (sumOfVoices * 0.01), 2)
			winnerNumber = str(j+1)
			nextCand = 0
		else:
			nextCand = round(votes[j] / (sumOfVoices * 0.01), 2)
			if nextCand > winnerPercent:
				winnerPercent = nextCand
				winnerNumber = str(j+1)
				count = 0
			elif nextCand == winnerPercent:
				count = 1
		if winnerPercent > 50:
			result = "majority winner " + winnerNumber
			return result
		elif j == n-1:
			if count == 0:
				result = "minority winner " + winnerNumber
			else:
				result = "no winner"
			return result
