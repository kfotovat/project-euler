def pythagorean_triplet():
    for a in xrange(1, 1000):
        for b in xrange(1, 1000):
            for c in xrange(1, 1000):
                if a*a + b*b == c*c and ((a + b + c) == 1000):
                    return a*b*c

print pythagorean_triplet()