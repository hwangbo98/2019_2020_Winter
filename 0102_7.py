int_list = []
remote_num = input()

remote_channel = [0,1,2,3,4,5,6,7,8,9,'+','-']
broke_count = int(input())

ok_remote  = []

broke_num = list(map(int, input().split()))

current_channel = 100

for i in range(len(remote_num)) :
    int_list.append(int(remote_num[i]))

ok_remote = list(set(remote_channel) - set(broke_num))
count = 0
k = 0
count2 = 1
count3 = 1
for x in (int_list) :
    if x in ok_remote :
        count+=1
    
    else :
        while(k>10) :
            if x+k in ok_remote :
                break
            count2+=1
                
            if x-k in ok_remote :
                break
            
            count3+=1
            
            k+=1
        
        min_count = min(count2,count3)
        
        
        
            


    

    



