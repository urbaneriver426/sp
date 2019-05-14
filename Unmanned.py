def Unmanned(N, L, data):
    dist = 0
    count = 0
    time = 0
    totalTime = 0

    if L == 0:
        return N

    for i in range(N):
        dist += 1
        if dist == data[count][0]:
            totalTime = data[count][1] + data[count][2]
            # общее время полного цикла светофора
            testTime = time - (totalTime * (time // totalTime))
            # время прошедшее от начала текущего цикла светофора
            if testTime < data[count][1] or testTime == totalTime:
                time += data[count][1] - testTime
            else:
                time += 1
            if count < L-1:
                count += 1
        else:
            time += 1
    return time
