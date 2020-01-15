list_str =[]
str_input = input()

for i in str_input :
    list_str.append(i)
    
count = 0
for j in list_str :
    if ((j == 'A') or (j == 'B') or (j == "C")) :
        count+=3
    
    elif ((j == 'D') or (j == 'E') or (j == 'F')) :
        count+=4
    
    elif ((j == 'G') or (j == 'H') or (j == 'I')) :
        count+=5
    
    elif ((j == 'J') or (j == 'K') or (j =='L')) :
        count+=6
    
    elif ((j == 'M') or (j == 'N') or (j == 'O')) :
        count+=7
    
    elif ((j == 'P') or (j == 'Q') or (j == 'R') or (j == 'S')) :
        count+=8
    
    elif ((j == 'T') or (j == 'U') or (j == 'V')) :
        count+=9
    
    elif ((j == 'W') or (j == 'X') or (j == 'Y') or (j == 'Z')) :
        count+=10
    
    else :
        count+=11
    
    print(count)
        
        
print(count)
    