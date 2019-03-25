def WordSearch(lens, s, subs):
    #start = 0
    #count = 0
    #point = 0
    #lines = 0
    test_arr = []
    test_arr2 = []
    #result = []
    #for i in range(len(s)):
    #    count += 1
    #    if s[i] == " ":
    #        if count == lens:
    #            test_arr.append([])
    #            lines = 0
    #            x = ""
    #            for j in range(start, (i+1)):
    #                x += s[j]
    #            test_arr[lines].append(x)
    #            lines += 1
    #            start = i+1
    #        elif count != lens:
    #            point = i
    #    elif count == lens or count - 
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
        if tes        

s = "строка разбивается на набор строк через выравнивание по заданной ширине."
lens = 12
s = "строка разбивается на набор строк через выравнивание по заданной ширине."
lens = 12
start = 0
test_arr = []
lines = 0
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

print(test_arr)

for i in range(len(test_arr)):
    if i !=len(test_arr[i])
