def shellSort(arr,n):
   gap=n//2
   while gap>0:
      for i in range(gap,n):
         temp=arr[i]
         j=i
         while j>=gap and arr[j-gap] >temp:
            arr[j]=arr[j-gap]
            j=j-gap
         arr[j] =temp
      gap=gap//2


data = list(map(int,input().split()))
size = len(data)
shellSort(data, size)
print(data)



