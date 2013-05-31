from lib import Primes, digits, num
from itertools import takewhile

primes = Primes()

def circular(p):
	d = digits(p)
	return all(primes.isPrime(num(d[i:] + d[:i])) for i in range(1, len(d)))

def main(limit):
	return sum(map(circular, takewhile(lambda n: n < limit, primes.gen())))

if __name__ == '__main__':
	print(main(1000000)) # 55
