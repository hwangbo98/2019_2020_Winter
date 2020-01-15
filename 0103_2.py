list_str = []
str_input = input()
set_str = []
count_str ={}
max_value = 0
count = 0
for j in str_input :
    list_str.append(j.upper())
    
set_str = list(set(list_str))

set_str.sort()

for k in set_str:
    if k in list_str :
        count_str[k] = list_str.count(k)
        
        
max_value = max(count_str.values())
for i in count_str.values() :
    if (max_value == i) :
        count+=1
for k in count_str.keys() :
    if (max_value == count_str.get(k) and count == 1) :
        print(k)
    if (count!=1) :
        print("?")
        break
    





    