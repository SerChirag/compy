def prime(x):
    s = set([])
    if(x%2 == 0):
        s.add(2)
    while(x%2==0):
        x /= 2
    for i in range(3,int(pow(x,0.5))+1,2):
        if(x%i==0):
            s.add(i)
            while(x%i==0):
                x /= i
    if(x>1):
        s.add(x)
    return s


