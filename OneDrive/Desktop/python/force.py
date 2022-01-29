n=int(input())
m=input()
l=input()
s=0
for i in range(n):
    a=abs(int(m[i]-int(l[i])))
    if a>5:
        a=10-a
    s=s+a    
print(s)        