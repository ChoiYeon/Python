#https://www.acmicpc.net/problem/2750
#버블 정렬 : 리스트랑세 인접한 두 수 를 비교 후 자리 swap 하여 정렬 

a =int(input())
b = []

for i in range(a):
    c = int(input())
    b.append(c)

for k in range(len(b)):
    for j in range(len(b)-1 ) :
        n1 = b[j]
        n2 = b[j+1]
        if(n1 > n2):
            b[j] = n2
            b[j+1] = n1

for m in range(len(b)):
    print(b[m])