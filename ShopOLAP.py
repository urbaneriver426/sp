def ShopOLAP (items):
    checkedItems = []
    prices = []
    result = []
    def LastLetter(s):
        return s[-1]

    for i in range(len(items)):
        count = 0
        if i == 0:
            checkedItems.append(items[0][0:len(items[0])-1])
            prices.append(int(items[0][-1]))
        else:
            item = items[i][0:len(items[i])-1]
            price = int(items[i][-1])
            for j in range(len(checkedItems)):
                if item == checkedItems[j]:
                    prices[j] += price
                    break
                elif j == len(checkedItems)-1:
                    checkedItems.append(items[i][0:len(items[i])-1])
                    prices.append(int(items[i][-1]))
        if i == len(items)-1:
            for j in range(len(checkedItems)):
                checkedItems[j] += str(prices[j])
        checkedItems.sort()
        checkedItems.sort(key=LastLetter, reverse=True)
