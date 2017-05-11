import itertools

def small_multiple(i):
    candidates = []
    m = i + 1
    for x in xrange(100000000
                   ,250000000,2):
    # for x in itertools.count(100):
        flag = True
        for j in range(2, m):
            if x % j != 0:
                flag = False
                # print x, j
                break
        if flag:
            candidates.append(x)
    return candidates

print small_multiple(20)