# cook your dish here
for t in range(int(input())):
    a,b,c=input().split()
    a,b,c=int(a),int(b),int(c)
    if((a*b)<0 or (b*c)<0 or (c*a)<0):
        print("YES")
    else:
        print("NO")
        