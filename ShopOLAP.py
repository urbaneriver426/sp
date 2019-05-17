def ShopOLAP (items):
    checkedItems = []
    prices = []

    for i in range(len(items)):
        if i == 0:
            checkedItems.append(items[0][0:len(items[0])-1])
            prices.append(int(items[0][len(items[0])-1:len(items[0])]))
        else:
            item = items[i][0:len(items[i])-1]
            price = int(items[i][len(items[i])-1:len(items[i])])
            for j in range(len(checkedItems)):
                if item == checkedItems[j]:
                    prices[j] += price
                else:
                    checkedItems.append(items[i][0:len(items[i])-1])
                    prices.append(int(items[i][len(items[i])-1:len(items[i])]))
        if i == len(items)-1:
            for j in range(len(checkedItems)):
                checkedItems[j] += str(prices[j])
            checkedItems.sort()
    
    return checkedItems
