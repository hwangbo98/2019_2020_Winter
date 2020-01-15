
num_input = int(input())

sum2 = 1
count = 0
sum1 = 1
while(1) :
    if (count>0) :
        sum2 += count*6
        sum1 = sum2 - ((count*6) +1)
        
    count+=1
    
    if (num_input >=sum1 and num_input<=sum2) :
        print(count)
        break
        
    
    


