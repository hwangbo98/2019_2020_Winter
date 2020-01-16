
money = int(input())
dp =[]

dp.append(0)
dp.append(1)
dp.append(2)
dp.append(2)
dp.append(2)
dp.append(1)
dp.append(2)
dp.append(1)

if money %7 == 0 :
    print(money//7)
else :    
    for i in range(8,money+1) :
        if i%7 == 0 :
           dp.append(i//7)
        
        else :
            dp.append((min(dp[i-5], min(dp[i-2], dp[i-1]))) + 1)
                    
    print(dp[money])
           
            
        