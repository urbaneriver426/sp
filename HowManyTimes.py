def HowManyTimes(s, s_generic):
	from copy import deepcopy
	result = 0
	listOfPositions = []

	for i in range(len(s_generic)):
		if s_generic[i] == s[0]:
			listOfPositions.append([i])

	testList = deepcopy(listOfPositions)
	count = 0

	for i in range(1, len(s)):
		testList = deepcopy(listOfPositions)

		count = 0

		for j in range(1,len(s_generic)):

			if s_generic[j] == s[i]:

				if count == 0:
		
					for k in range(len(listOfPositions)):

						if listOfPositions[k][len(listOfPositions[k])-1] < j:
							listOfPositions[k].append(j)
							count = 1

				elif count != 0:
					temporaryList = deepcopy(testList)
					
					for k in range(len(temporaryList)):
	
						if temporaryList[k][len(temporaryList[k])-1] < j:
	
							temporaryList[k].append(j)
	
					listOfPositions = listOfPositions + temporaryList

	for i in range(len(listOfPositions)):
		if len(listOfPositions[i]) == len(s):
			result += 1

	return result
