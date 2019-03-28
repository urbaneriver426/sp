def WordSearch(lens, s, subs):
    start = 0 
    count = 0 
    point = 0 
    lines = 0 
    test_arr1 = [] 
    test_arr2 = [] 
    result = [] 
    x = ""
    y = ""

    for i in range(len(s)):
        x += s[i]
        if s[i] == " " or i == len(s)-1:
            test_arr1.append(x)
            lines += 1
            x = ""
            y = ""

    for i in range(len(test_arr1)):
        if i == 0: 
            lines = 0
            if len(test_arr1[i]) <= lens: 
                test_arr2.append(test_arr1[i]) 
            else: 
                x = test_arr1[i] 
                for j in range(len(x)): 
                        count += 1 
                        y += x[j] 
                        if count == lens: 
                            test_arr2.append(y) 
                            y = "" 
                            count = 0 
                        if j == len(x)-1: 
                            if count == 1 and y == " ": 
                                if i < len(test_arr1)-1: 
                                    test_arr2.append("") 
                                    lines += 1 
                                    y = ""
                            else: 
                                test_arr2.append(y) 
                                lines += 1 
                                if i < len(test_arr1)-1: 
                                    test_arr2.append("") 
                                    lines += 1 
                                    y = ""

        else: 
            x = test_arr1[i]
            if len(test_arr2[lines])+len(x) <= lens: 

                test_arr2[lines] = test_arr2[lines] + x 

            elif len(test_arr2[lines])+len(x) >= lens: 

                if len(test_arr2[lines])+len(x[0:(len(x)-1)]) == lens: 
                    if x[len(x)-1] == " ":
                        test_arr2[lines] = test_arr2[lines] + x[0:(len(x)-1)]
                    else:
                    	test_arr2.append(x) 
                    	lines += 1
                
                elif len(x) <= lens: 
                    test_arr2.append(x) 
                    lines += 1 

                elif len(x) > lens: 
                    
                    if len(x) == lens+1: 
                        if len(test_arr2[lines]) == 0:
                            test_arr2[lines] = test_arr2[lines] + x[0:(len(x)-1)]
                        else:
                            test_arr2.append(x[0:(len(x)-1)]) 
                            lines += 1 

                    else:
                        for j in range(len(x)): 
                            count += 1 
                            y += x[j] 
                            if count == lens: 
                                if len(test_arr2[lines]) == 0:
                                    test_arr2[lines] = test_arr2[lines] + y
                                    y = "" 
                                    count = 0 
                                else:
                                    test_arr2.append(y)
                                    lines += 1 
                                    y = "" 
                                    count = 0 
                            if j == len(x)-1: 
                                if count == 1 and y == " ": 
                                    if i < len(test_arr1)-1:
                                        test_arr2.append("") 
                                        lines += 1 
                                        y = ""
                                else: 
                                    test_arr2.append(y) 
                                    lines += 1 
                                    if i < len(test_arr1)-1: 
                                        test_arr2.append("") 
                                        lines += 1 
                                        y = ""                

    for i in range(len(test_arr2)):
        x = test_arr2[i]
        y = ""
        result.append(0)
        for j in range(len(x)):
            if x[j] == " ":
                if y == subs:
                    result[i] = 1
                y = ""
            else:
                y += x[j]
            if j == len(x)-1:
                if y == subs:
                    result[i] = 1

    return result
