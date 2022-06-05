n=int(input('введите число  '))
k=0
s=[]
s1=[]
for i in range(1,n+1,2):
    s1=[]
    k=n//2
    n -= 2
    for j in range(-k,0):
        s1.append(' ')
    if i==1:
        s.append('*')
    else:
        s.append('*')
        s.append('*')
    print(''.join(s1), ''.join(s))