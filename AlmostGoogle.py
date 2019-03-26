def WordSearch(lens, s, subs):
    start = 0
    count = 0
    point = 0
    lines = 0
    test_arr = []
    test_arr2 = []
    result = []
    for i in range(len(s)):
        if s[i] == " ":
            test_arr.append([])
            lines += 1
            x = ""
            for j in range(start, i+1):
                x += s[j]
            test_arr[lines-1].append(x)
            if i != len(s)-1:
                start = i+1
        elif i == len(s)-1:
            test_arr.append([])
            lines += 1
            x = ""
            for j in range(start, i+1):
                x += s[j]
            test_arr[lines-1].append(x)

    for i in range(len(test_arr)):
        if i == 0:
            test_arr2.append(test_arr[i])
            lines = 0
        else:
            if len(test_arr2[lines][0])+len(test_arr[i][0]) <= lens:
                test_arr2[lines][0] = test_arr2[lines][0]+test_arr[i][0]
                test_arr2.append([])
                count += 1
                test_arr2[lines].append("")
            elif len(test_arr2[lines][0])+len(test_arr[i][0]) > lens:
                if len(test_arr[i][0]) <= lens:
                    lines += 1
                    test_arr2.append(test_arr[i])
                else:
                    if len(test_arr2[lines][0]) == 0:
                        x = test_arr[i][0]
                        for j in range(len(x)):
                            count += 1
                            if count == 1:
                                y = x[j]
                                if count == 1 and j == len(x)-1 and y = " ":
                                    test_arr2.append([])
                                    lines += 1
                                    test_arr2[lines].append("")
                            else:
                                y += x[j]
                                if j == lens-1:
                                    test_arr2[lines][0] = test_arr2[lines][0]+y
                                elif count == lens:
                                    test_arr2.append([])
                                    lines += 1
                                    test_arr2[lines].append(y)
                                elif j == len(x)-1:
                                    test_arr2.append([])
                                    lines += 1
                                    test_arr2[lines].append(y)

                    else:
                        x = test_arr[i][0]
                    for j in range(len(x)):
                        if j == 0 or j == lens:
                            y = x[j]
                        else:
                            y += x[j]
                        if j == lens-1:
                            test_arr2.append([])
                            lines += 1
                            test_arr2[lines].append(y)
                        elif j == len(x)-1:
                            test_arr2.append([])
                            count += 1
                            test_arr2[lines].append(y)
    return test_arr2
