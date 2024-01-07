a=[1,2,3,4]
n=input('enter the index:')
v=input('enter the value:')
y=len(a)
if v in a:
    for i in range(y):
        if a[i]==v:
            a.insert(i+1,v)
            break
print(a)