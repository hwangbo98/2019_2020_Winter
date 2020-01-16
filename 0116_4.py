num_of_fruits = int(input())

total_num = int(input())

rest_num = total_num - num_of_fruits

edit_total_num = num_of_fruits + rest_num -1
boonsu = 1
boonmo = 1

for i in range(edit_total_num,rest_num,-1) :
    boonsu*=i

for j in range(edit_total_num - rest_num, 0,-1) :
    boonmo*=j 

 
result = boonsu // boonmo

print(result)
    
