def method1(num):
    a = [1, 1]
    for i in range(2,num):
        a.append(a[i-1] + a[i-2])
    print 'By method 1', a
    
    
def method2(num):
    b = [1, 1]
    [b.append(b[k-1]+b[k-2]) for k in range(2,num)] 
    print 'By method 2', b

def method3(num):
    """ Golden Ratio Method"""
    print 'By method 3',
    print [int((((1 + 5**0.5) / 2)**n - ((1 - 5**0.5) / 2)**n) / 5**0.5) for n in range(1, num + 1)]
    

def main():
    num = input('Enter how many numbers do you want in Fibonacci Series:')
    method1(num)
    method2(num)
    method3(num)


if __name__ == '__main__':
    main()
