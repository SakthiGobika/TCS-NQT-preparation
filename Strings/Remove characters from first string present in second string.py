s1=input()
s2=input()
res=""
for i in s1:
    if i not in s2:
        res+=i
print(res)