
str_input = int(input())
list_num = []
count = 0
i = 0
while(True) :
    cal_str = ""+ str(count)
    
    if "666" in cal_str :
        i+=1
    
    if (i == str_input) :
        break
    
    count+=1

print(cal_str)
