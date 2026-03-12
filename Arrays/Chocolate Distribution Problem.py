'''Q- Chocolate Distribution Problem 
Problem Statement: A teacher has N packets of chocolates, each containing some number of chocolates. She wants to distribute these packets among M students such that each student receives exactly one packet. 
The goal is to minimize the difference between the maximum and minimum chocolates received by the students.
 Find the minimum possible difference. 
 Input Format: . First line: integer N . 
 Second line: N space-separated integers (packets) . 
 Third line: integer M 
 Output Format: . Print the minimum difference.'''
n=int(input())
packets=list(map(int,input().split()))
m=int(input())
packets.sort()
mindiff=float('inf')
for i in range(n-m+1):
    f=packets[i]
    l=packets[i+m-1]
    diff=l-f
    if diff<mindiff:
        mindiff=diff
print(mindiff)