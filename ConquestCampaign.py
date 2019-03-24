def ConquestCampaign(N,M,L,battalion):
    sqr = []
    days = 1
    count = 1
    for i in range(N):
        sqr.append([])
        for j in range(M):
            sqr[i].append(0)
    for i in range(0,len(battalion),2):
        sqr[battalion[i]-1][battalion[i+1]-1] = 1
    while count != 0:
        days += 1
        count = 0
        for i in range(1):
            for j in range(N):
                for k in range(M):
                    if k == 0 and sqr[j][k] == 0:
                        if sqr[j][k+1] == days-1:
                            sqr[j][k] = days
                    elif sqr[j][k] == 0 and k < M - 1:
                        if sqr[j][k-1] == days-1:
                            sqr[j][k] = days
                        elif sqr[j][k+1] != 0:
                            sqr[j][k] = days
                    elif sqr[j][k] == 0 and k == M - 1:
                        if sqr[j][k-1] == days-1:
                            sqr[j][k] = days
                    if sqr[j][k] == days-1:
                        if j != 0:
                            if sqr[j-1][k] == 0:
                                sqr[j-1][k] = days
                        if j != N-1:
                            if sqr[j+1][k] == 0:
                                sqr[j+1][k] = days
        for i in range(N):
            for j in range(M):
                if sqr[i][j] == 0:
                    count = 1
                    break
    return days
