def LineAnalysis(line):
    for i in range(len(line)):
        if i == 0 or i % 3 == 0:
            if line[i] != "*":
                return False
        else:  
            if line[i] != ".":
                return False
    return True
