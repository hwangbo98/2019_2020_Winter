int_list = []
remote_num = input()

remote_channel = [0,1,2,3,4,5,6,7,8,9,'+','-']
broke_count = int(input())

ok_remote  = []

broke_num = list(map(int, input().split()))

current_channel = 100

for i in range(len(remote_num)) :
    int_list.append(int(remote_num[i]))

ok_remote = list(set(remote_channel) - set(broke_num))

print(ok_remote)

    

    



