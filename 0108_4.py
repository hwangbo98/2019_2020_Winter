from collections import deque

list_str = deque()

num = int(input())

for i in range(num) :
    list_str.append(i+1)
count = 0  
while(True):
    count+=1
    if len(list_str)==1 :
        break
    else :
        if count%2 == 1 :
            list_str.popleft()
        else :
            
            list_str.append(list_str[0])
            list_str.popleft()
    
        


for i in list_str :
    print(i)
    

    