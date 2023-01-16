# cook your dish here
for t in range(int(input())):
    n=int(input())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    arr=arr1+arr2
    #print(arr)
    arr.sort()
    mini=arr[(2*n)-1] - arr[0]
    for i in range(0,n+1):
        mini=min(mini,(arr[n+i-1] - arr[i]))
        #print("arr[n+i-1] = ",arr[n+i-1],"arr[i] = ",arr[i])
    print(mini)
        
        