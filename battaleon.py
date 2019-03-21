x = 3
y = 3
l = 1
arr = [2,2]
painted = []
count = 0
days = 1
for i in range(x+1):
    painted.append([])
for i in range(l):
    painted[arr[i]].append(arr[i+1])
    count += 1
#while count != x*y:
#    for i in range(painted):
#        for j in range(len(painted[i]):
#            if painted[i][j] < 0 
for i in range(len(painted)):
    for j in range(len(painted)):
        for j in range(len(painted[i])):
            if i > 1 and i < y:
                painted[i-1].append(painted[i][j])


print(painted)
    
