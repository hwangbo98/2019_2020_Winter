from collections import deque
list_num = list(map(int, input().split(" ")))

numbers = []
result = []
total_num = list_num[0]

which_num = list_num[1]

for i in range(total_num) :
    numbers.append(i+1)

count = 0
while(True) :
    for i in numbers :
        count+=1
        if count == which_num :
            result.append(i)
            count = 1
            numbers.remove(i)
        
    if len(result) == total_num :
        break


print("<", end= "")
count_num = 0
for i in result :
    count+=1
    if count == len(result) :
        print(i, end= " ")
    else :
        print(str(i)+",", end= " ")

    
print(">", end = "")



