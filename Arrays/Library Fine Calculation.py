'''Q- Library Fine Calculation 
Problem Statement: A library keeps track of books borrowed by students. 
Each element in the array represents the number of days a student kept a book. If a book is kept more than K days, the student must pay 1 unit fine for each extra day. Find the total fine collected.
 Input Format: . First line: integer N . Second line: N space-separated integers . Third line: integer K
 Output Format: . Print total fine. explain me with problem statemnet input'''
n=int(input())
days=list(map(int,input().split()))

k=int(input())
f=0
##l=[]
for i in days:
    if i>k:
        f+=(i-k)
print(f)