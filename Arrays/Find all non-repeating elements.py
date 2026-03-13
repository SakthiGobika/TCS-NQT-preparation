arr=list(map(int,input().split()))
seen=set()
# res=[]
# for i in arr:
#     if i not in seen:
#         seen.add(i)
#     else:
#         res.append(i)
    
# print(res)
freq={}
for i in arr:
    freq[i]=freq.get(i,0)+1
res=[]
for i,j in freq.items():
    if j==1:
        res.append(i)
if len(res)!=0:
    print(res)
else:
    print(-1)

