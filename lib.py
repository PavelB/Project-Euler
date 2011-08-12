from itertools import count, combinations, product
from math import sqrt

class Primes:
	computed = None
	computedLen = 0

	def __init__(self):
		self.compute(1024)

	def compute(self, n): # compute all primes <= n
		# http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
		nroot = int(sqrt(n))
		sieve = [True] * (n + 1)
		sieve[0] = False
		sieve[1] = False
		for i in range(2, nroot + 1):
			if sieve[i]:
				sieve[i * i: n + 1:i] = [False] * (n // i - i + 1)
		self.computed = [i for i in range(n + 1) if sieve[i]]
		self.computedLen = len(self.computed)

	def get(self, i): # get the i-th prime, zero indexed
		lim = self.computedLen
		while i >= self.computedLen:
			lim *= 2
			self.compute(lim)
		return self.computed[i]

	def gen(self, limit = float('inf')): # return a generator of primes <= limit
		for i in count():
			p = self.get(i)
			if p > limit:
				break
			yield p

	def factors(self, n):
		rootn = sqrt(n)
		for p in self.gen():
			if p > rootn:
				break
			exp = 0
			while n % p == 0:
				exp += 1
				n //= p
			if exp > 0:
				rootn = sqrt(n)
				yield p, exp
		if n > 1:
			yield n, 1

	def divisors(self, n, proper = False):
		if n > 0:
			parts = list([pow(b, i) for i in range(1, e + 1)] for b, e in self.factors(n))
			for k in range(len(parts) + 1):
				for tuples in combinations(parts, k):
					for tuple in product(*tuples):
						d = multiply(tuple)
						if proper and d == n:
							return
						yield d

	def isPrime(self, n):
		return n > 1 and all(b == 1 or b == n for b, _ in self.factors(n))

def multiply(iterator):
	rv = 1
	for n in iterator:
		if n == 0:
			return 0
		rv *= n
	return rv

def digits(n):
	rv = []
	while True:
		rv.append(n % 10)
		n //= 10
		if n == 0:
			return reversed(rv)

def num(digits):
	n = 0
	for d in digits:
		n = 10 * n + d
	return n