from lib import num
from itertools import product, count, takewhile, chain

def palindromes(base=10):
	def fronts(r, base):
		if r == 0:
			yield tuple()
		else:
			for first in range(1, base):
				for rest in product(range(base), repeat=r - 1):
					yield tuple([first]) + rest
	for r in count():
		for half in fronts(r, base):
			for middle in range(base):
				yield num(chain(half, [middle], reversed(half)))
		for half in fronts(r + 1, base):
			yield num(chain(half, reversed(half)))

def toDec(n, base):
	rv = 0
	p = 1
	while n > 0:
		rv += (n % 10) * p
		n //= 10
		p *= base
	return rv

def main(limit):
	good = lambda n: n < limit
	base2pal = takewhile(good, (toDec(n, 2) for n in palindromes(2)))
	base10pal = takewhile(good, palindromes(10))
	return sum(set(base2pal) & set(base10pal))

print(main(1000000))