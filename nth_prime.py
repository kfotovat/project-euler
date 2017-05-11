import itertools

def nth_prime(n):
    l = []
    for i in itertools.count(2):
        flag = True
        for j in xrange(2,i-1):
            if i%j == 0:
                flag = False
                break
        if flag:
            l.append(i)
            if len(l) == n:
                return l[-1]

print nth_prime(10001)