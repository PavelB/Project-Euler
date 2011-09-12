from lib import num, digits, palindrome

def seq(n, lim = 54):
	for _ in range(lim):
<<<<<<< HEAD
		n += num(reversed(digits(n)))
=======
		n += num(reversed(list(digits(n))))
>>>>>>> upstream/master
		yield n

def lycharel(n):
	return not any(map(palindrome, seq(n)))

def main(lim):
	return sum(map(lycharel, range(1, lim)))

print(main(10000)) # 249
