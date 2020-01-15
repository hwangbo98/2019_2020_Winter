
str_input = input()
list_str =[]
for i in str_input :
    list_str.append(i)

count = 0 
count2 = 0
for j in range(len(list_str)) :
    if list_str[j] == 'c' :
        if list_str[j+1] == '=' or list_str[j+1] == '-' :
            count+=1
        
        else :
            count+=1
    
    elif list_str[j] == 'd' :
        if list_str[j+1] == '-' :
            count+=1
        
        elif list_str[j+1] == 'z' :
            if list_str[j+2] == '=' :
                count+=1
        
        else :
            count+=1
                
    elif list_str[j] == 'l' :
        if list_str[j+1] == 'j' :
            count+=1
        else :
            count+=1
    
    elif list_str[j] == 'n' :
        if list_str[j+1] == 'j' :
            count+=1
        else :
            count+=1
    
    elif list_str[j] == 's' :
        if list_str[j+1] == '=' :
            count+=1
        else :
            count+=1
    
    elif list_str[j] == 'z' :
        if list_str[j-1] == 'd' and list_str[j+1] == '=' :
            pass
        else :
            count+=1
        

    elif list_str[j].isalpha() :
        count2+=1
    
    
            

print(abs(count))


