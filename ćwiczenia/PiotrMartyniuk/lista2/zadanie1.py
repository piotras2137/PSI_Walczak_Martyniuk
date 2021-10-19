a_list = [i for i in range(10,0,-1)]
b_list = [i for i in range(0,9,1)]

print(a_list)
print(b_list)
x = 0 

if len(a_list) > len(b_list):
    x = len(a_list)
else:
    x = len(b_list)


for i in range(0,x):
    if i%2==0 and len(a_list) > i:
        print(a_list[i])
    elif len(b_list) > i and i%2!=0:
        print(b_list[i])