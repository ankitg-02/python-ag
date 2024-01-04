#reverse
def reverse(a):
    r=0
    while a%10!=0:
        ar=a%10
        r=r*10+ar
        a=a//10
    return r
a=int(input('enter a num:'))
b=reverse(a)
print('reverse of {} :{}'.format(a,b))


