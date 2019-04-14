list_=[int(x) for x in input().split()]
res=[]
n=len(list_)
for i in range(n):
    for j in range(i,n+1):
        res.append(list_[i:j])
print(res)
