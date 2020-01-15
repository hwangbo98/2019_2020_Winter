
S = "ab##"
T = "c#d#"

S_list = list(S)
T_list = list(T)

for i in range(len(S_list)) :
    if S_list[i] == '#' :
        S_list.pop(i) 
        S_list.pop(i-1)
    else :
        pass
    
for j in range(len(T_list)) :
    if T_list[j] == '#' :
        T_list.pop(j)
        T_list.pop(j-1)

S_str = ' '.join(S_list)
T_str = ' '.join(T_list)

if S_str in T_str :
    print(True)
else :
    print( False )