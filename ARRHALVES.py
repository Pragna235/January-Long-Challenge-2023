# cook your dish here
for t in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    diff1=[]
    diff2=[]
    for i in range(len(arr)):
        if(arr[i]>n and i<n):
            diff1.append(i+1)
        if(arr[i]<=n and i>=n):
            diff2.append(i+1)
    diff1.sort()
    diff2.sort()
    p=0
    n=len(diff1)
    for i in range(n):
        p+=abs(diff1[i] - diff2[i])
        
    print(p)