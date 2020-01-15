cnt = 0;
N = int(input())
for i in range(N):
    check= [0]*26
    flag = 1;
    word = input()
    n = len(word)
    
    for j in range(n):
        if check[ord(word[j])- 97]:
            if word[j] != word[j-1]:
                flag = 0;
                break
        check[ord(word[j])-97] = 1
    check = [0]*26
    
    if flag:
        cnt +=1
print(cnt)