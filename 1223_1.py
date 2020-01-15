num_list = list(map(int, input().split()))

count1 = 0
count2 = 0

for i in range(1,len(num_list)) :
    if (num_list[i] - num_list[i-1] == 1) :
        count1+=1
    
    elif (num_list[i] - num_list[i-1] == -1) :
        count2+=1
    else :
        print("mixed")
        break   
    
    if (count1 == 7) :
        print("ascending")
    
    if (count2 == 7) :
        print("decending")
    '''   
    if ((num_list[i] - num_list[i-1] != 1) or (num_list[i] - num_list[i-1] != -1))  :
        print("mixed")
        break'''
    
    
        
    
    

