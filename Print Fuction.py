if _name_ == '_main_':
    n = int(input())
    sum=0
    for i in range(1,n+1) :
        if i<10 :
            sum=sum*10+i
        elif i<100 :
            sum=sum*100+i
        else :
            sum=sum*1000+i
    print(sum)
