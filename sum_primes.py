def primes_comp(n): 
    return sum([i for i in xrange(2, n) for j in xrange(2, n-1) if i%j != 0])

def sum_primes(n):
    primes = []
    for i in xrange(2, n):
        for j in xrange(2, n-1):
            flag = True
            if i%j == 0:
                flag = False
        if flag:
            primes.append(i)
    return sum(primes)

# print sum_primes(6)
print sum_primes(1000000)
# print primes_comp(6)