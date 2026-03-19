arr=list(map(int,input().split()))
if len(arr)!=0:
    c=1
    maxi=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>maxi:
            c+=1
            maxi=arr[i]
    print(c)
else:
    print(0)
