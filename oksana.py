def odometr (oksana):
    for i in range(len(oksana)):
        if i == 1:
            distanse = oksana[i] * oksana[i-1]
        elif i%2 != 0:
            distanse += oksana[i-1] * (oksana[i] - oksana[i-2])
    return distanse
