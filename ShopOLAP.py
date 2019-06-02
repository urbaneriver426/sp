def ShopOLAP (n, items):
	checkedItems = []
	prices = []

	def LastNumber(s):
		x = ""
		count = 0
		for i in range(len(s)):
			if count != 0:
				x += s[i]
			elif s[i] == " ":
				count = 1
		return int(x)

	for i in range(len(items)):
		count = 0
		for j in range(len(items[i])-1,0,-1):
			if items[i][j] != " ":
				count += 1
			else:
				item = items[i][0:len(items[i])-count]
				price = int(items[i][len(items[i])-count:len(items[i])])
				if i == 0:
					checkedItems.append(item)
					prices.append(price)
				else:
					for k in range(len(checkedItems)):
						if item == checkedItems[k]:
							prices[k] += price
							break
						elif k == len(checkedItems)-1:
							checkedItems.append(item)
							prices.append(price)
				break
		if i == len(items)-1:
			for j in range(len(checkedItems)):
				checkedItems[j] = checkedItems[j] + str(prices[j])
			prices.sort(reverse=True)

	checkedItems.sort()
	checkedItems.sort(key=LastNumber, reverse=True)

	return checkedItems
