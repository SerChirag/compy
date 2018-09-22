# generate prime number using Seive of Erathanos
def seive(max_num):
    max_num += 1 #include the number itself
    prime = [0]*max_num
    for i in range(2,max_num):
        if(prime[i] == 0):
            for j in range(i*i,max_num,i):
                prime[j] = i
    for i in range(2,max_num):
        if(prime[i] == 0):
            prime[i] = i
    return prime


def prime_factorize(spf,x):
    p = {} #store prime numbers
    while(x>1):
        curr_prime = spf[x]
        p[curr_prime] = 1
        while(x%curr_prime == 0): #keep dividing till all powers of current prime are gone
            x = x/curr_prime
    return p





max_num = 150001
spf = seive(max_num)
print prime_factorize(spf,12246)