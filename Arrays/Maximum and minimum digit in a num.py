n=int(input())
maxi=float('-inf')
mini=float('inf')
if n<0:
    n=n*-1
if n<=9:
    print("Maximum digit is",n)
    print("Minimum digit is",n)
else:
    l=[]
    while n>0:
        d=n%10
        l.append(d)
        n//=10
    for i in l:
        if i>maxi:
            maxi=i
        if i<mini:
            mini=i
    print("Maximum digit is",maxi)
    print("Minimum digit is",mini)


