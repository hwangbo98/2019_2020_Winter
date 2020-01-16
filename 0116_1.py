num = int(input())
list_str = []
push_door = 1
pull_door = 0

start_num = int(input())
list_str.append(start_num)

if num >=6 :
    print("Love is open door")
else :
    for i in range(1,num) :
        if start_num == 1 :
            if ((i+1)%2) == 0 :
                list_str.append(pull_door)
            elif ((i+1)%3) == 0 :
                list_str.append(push_door)
                
            else :
                list_str.append(push_door)
                
        elif start_num == 0 :
            if ((i+1)%2) == 0 :
                list_str.append(push_door)
            elif ((i+1)%3) == 0 :
                list_str.append(pull_door)
                
            else :
                list_str.append(pull_door)
            
    
    for i in range(1,num) :
        print(list_str[i])          