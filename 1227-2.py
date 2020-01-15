
how_many = int(input(""))
max_point = 0
standard_point = 0
final_result = []

num_list = list(map(int, input().split()))

print(num_list)
    
for j in range(1,how_many):
    if num_list[j-1] < num_list[j] :
        count+= num_list[j] - num_list[j-1];
        
    else :
        count = 0
        
    if max < count :
        max = count
    
        
        
print(max)
    
