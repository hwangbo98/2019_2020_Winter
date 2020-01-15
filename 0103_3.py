word_count = int(input())
str_input = []
result = []
for i in range(word_count) :
    str_input.append(input())
    


for k in range(word_count) :
    result.append(str_input[k][0])
    for j=k+1 in range(1,len(str_input[k])) :
        if (str_input[k][j] != str_input[k][j-1]) :
            result.append(str_input[k][j])
            
            
            
print(result)