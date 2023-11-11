#https://www.acmicpc.net/problem/2587

b = []
mod = 0
sum = 0

for i in range(5):
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
   sum += b[m] 

mod = sum // len(b)
mid = b[len(b)//2]
print(mod)
print(mid)