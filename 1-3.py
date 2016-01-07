import random
x=input('please input a number:')
i=0
a=[1,2,3]
b=[4,5,6]
c=[7,8,9]
if not x:
    n=5
else :
    n=int(x)
while i<n:
    m=[]
    d=random.randint(1,2) 
    if d==1:
        m.append(random.choice(a))
        m.append(random.choice(b))
        m.append(random.choice(c))
    if d==2:
        m.append(random.choice(a))
        m.append(random.choice(c))
    print(m)
    i+=1
    
    
