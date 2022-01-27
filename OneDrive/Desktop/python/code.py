n=int(input())
l=list(map(int,input().split()))
c=0
k=[]
for i in range(n-1):
    if l[i]<l[i+1]:
        c=c+1
    else:
        k.append(c)
        c=0
k.append(c)
k.sort()
p=k[-1]+1 
print(k)       
print(p)        
    

