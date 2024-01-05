a=[2,3,4]
b=[6,7,8]
c=[]
m=len(a)
n=len(b)
l=max(len(a),len(b))
for i in range(l):
    if i<m:
        c.append(a[i])
    if i<n:
        c.append(b[i])
print(c)