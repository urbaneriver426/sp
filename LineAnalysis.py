def LineAnalysis(line):
    count = 1
    point = 0

    if line[0] != "*" or line[len(line)-1] != "*":
        return False

    for i in range(1,len(line)):
        if point == 0:
            if line[i] == ".":
                count += 1
            elif line[i] == "*":
                point = i
        else:
            if line[i] == "*":
                if i - point == count:
                    point = i
                else:
                    return False
            elif line[i] == ".":
                if i - point >= count:
                    return False
    return True
