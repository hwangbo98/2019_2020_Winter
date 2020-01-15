str_s = "baby sukhwan tururu turu very cute tururu turu in bed tururu turu baby sukhwan "
list_str = []
count = 0
another_list =[]
for char in str_s.split() :
    another_list.append(char)



choose_num = int(input())
total_num = 0

while(True) :
    if total_num == choose_num :
        break
    for char in another_list :
        if char == "tururu" :
            if count+2<5 :
                list_str.append("tu" + "ru"*(count+2))
            else :
                list_str.append("tu"+"+"+"ru*"+str(count+2))
        elif char == "turu" :
            if count+1<5 :
                list_str.append(char + "ru"*(count+1))
            else :
                list_str.append("tu" "+" "ru*"+str(count+1))
        elif char == "" :
            pass
        else :
            list_str.append(char)
        total_num +=1
    
        if total_num == choose_num :
            print(list_str[total_num-1])
            break
    
      
            
    count+=1
    
