'''Q1 - Maximum and Minimum digit in a Number

Problem Statement:
Given an integer N, find and print the smallest digit and largest digit present in the number.

Input Format:
· A single integer N

Output Format:
. Print two integers separated by space:
Minimum Digit Maximum Digit

Constraints:
· 1 SN ≤ 10**9
'''
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


