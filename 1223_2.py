
list_sum = []
for i in range(5) :
    list_num = list(map(int, input().split()))
    sum = 0
    for j in range(len(list_num)) :
        sum += list_num[j]
    list_sum.append(sum)
    

max = 0
count = 0
for k in range(len(list_sum)) :
    if list_sum[k] > max :
        max = list_sum[k]
        count = k
        
        
print(count+1,max)
 
   