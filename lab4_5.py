m=['ankit','goutam','']
n=[]
for i in range(0,len(m)+1):
    if m!='':
        n.remove(m[i])
        break
    else:
        n.append(m[i])
print(n)