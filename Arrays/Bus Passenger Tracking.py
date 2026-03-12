'''Q - Bus Passenger Tracking 
Problem Statement: A bus travels through several stations. At each station: . Some passengers get off · Some passengers get on Find the maximum number of passengers in the bus at any time. 
Input Format: . First line: integer N (number of stops) . Next N lines contain two integers: · passengers getting off · passengers getting on 
Output Format: · Print maximum passengers in bus.'''
n=int(input())
c=0
maxi=0
for i in range(n):
    a,b=map(int,input().split())
    c=(c-a)+b
    if c>maxi:
        maxi=c
print(maxi)
