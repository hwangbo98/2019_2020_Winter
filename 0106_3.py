how_many = int(input())
hei_wei = []
for i in range(how_many) :
    s = list(map(int, input().split()))
    hei_wei.append(s)

  

for i in range(how_many) :
    count = 1
    for j in range(how_many) :
        if ((hei_wei[i][0]< hei_wei[j][0]) and (hei_wei[i][1] < hei_wei[j][1])) :
            count+=1
            
    print(count, end=' ')
        
