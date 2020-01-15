
num_input = int(input())

str_input = list(map(int, input().split()))


set_list = sorted(str_input)

result = list(set(set_list))
for i in result :
    print(i, end=" ")


