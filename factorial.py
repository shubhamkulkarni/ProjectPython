def fact(num):
    i,out = 0,1
    for i in range(1,num+1):
        out=i*(out)
    print out
fact(5)
