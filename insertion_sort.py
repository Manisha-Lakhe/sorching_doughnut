li = []
li = list(map(int,input().split()))
for i in range(len(li)):
    for j in range(i + 1,len(li)):
        while li[i] > li[j]:
            li[i] , li[j] =  li[j] , li[i]
print(li)



