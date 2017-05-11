def primes_sieve(n):
	size = n/2
	sieve = [1]*size
	limit = int(n**0.5)
	for i in range(1, limit):
		if sieve[i]:
			val = 2*i+1
			tmp = ((size-1)-i)/val
			sieve[i+val::val] = [0]*tmp
	return [2] + [2*i+1 for i,v in enumerate(sieve) if v and i>0]


print sum(primes_sieve(2000000))