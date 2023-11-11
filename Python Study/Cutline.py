#https://www.acmicpc.net/problem/25305

a,n =map(int ,input().split(" "))
b = []

b = list(map(int , input().split(" ")))

for k in range(len(b)):
    for j in range(len(b)-1 ) :
        n1 = b[j]
        n2 = b[j+1]
        if(n1 < n2):
            b[j] = n2
            b[j+1] = n1

print(b[n-1])