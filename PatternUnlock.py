def PatternUnlock(N, hits):
    curr = hits[0]
    prvs = 0
    count = 0
    password = ""
    for i in range(N):
        prvs = curr
        curr = hits[i]
        if curr == 1:
            if prvs == 6 or prvs == 2 or prvs == 9:
                count += 1
            if prvs == 5 or prvs == 8:
                count += 1.41421
        if curr == 2:
            if prvs == 1 or prvs == 3 or prvs == 5 or prvs == 8:
                count += 1
            if prvs == 6 or prvs == 4 or prvs == 9 or prvs == 7:
                count += 1.41421
        if curr == 3:
            if prvs == 2 or prvs == 4 or prvs == 7:
                count += 1
            if prvs == 5 or prvs == 8:
                count += 1.41421
        if curr == 4:
            if prvs == 5 or prvs == 3:
                count += 1
            if prvs == 2:
                count += 1.41421
        if curr == 5:
            if prvs == 6 or prvs == 2 or prvs == 4:
                count += 1
            if prvs == 1 or prvs == 3:
                count += 1.41421
        if curr == 6:
            if prvs == 1 or prvs == 5:
                count += 1
            if prvs == 2:
                count += 1.41421
        if curr == 7:
            if prvs == 3 or prvs == 8:
                count += 1
            if prvs == 2:
                count += 1.41421
        if curr == 8:
            if prvs == 9 or prvs == 2 or prvs == 7:
                count += 1
            if prvs == 1 or prvs == 3:
                count += 1.41421
        if curr == 9:
            if prvs == 1 or prvs == 8:
                count += 1
            if prvs == 2:
                count += 1.41421
    count = list(str(count))
    for i in range(len(count)):
        if count[i] != "." and count[i] != "0":
            password += count[i]
    return password
