def ShopOLAP (n, items):
	result = []
	checkedItems = {}

	for i in range(len(items)):
		item = items[i].split()
		if checkedItems.get(item[0]) == None:
			checkedItems[item[0]] = int(item[1])
		else:
			checkedItems[item[0]] += int(item[1])

	sortedItems = sorted(checkedItems.items())
	sortedItems.sort(key=lambda couple: couple[1], reverse=True)
	
	for i in sortedItems:
		result.append(i[0] + " " + str(i[1]))

	return result
