a=[]
i=0
total=0
count=0
while i>=0:
    b=input('please input a number or enter to finish:')
    if b :
        num=int(b)
        a.append(num)
        total+=1
        count+=num
        maximum=a[0]
        minimum=a[0]
        if num>maximum:
            maximum=num
        if num<minimum:
            minimun=num
    ave=(count/total)
    if not b:
        if (total-1)%2==0:
            c=int((total-1)/2)
            d=a[c]
        else:
            e=int((total)/2)
            f=int((total)/2-1)
            d=(a[e]+a[f])/2
        print(a,total,count,maximum,minimum,ave,d)
        break
