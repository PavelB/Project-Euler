from lib import pythagoreanTriples

def main(n):
	return next(a * b * c for a, b, c in pythagoreanTriples() if a + b + c == n)

if __name__ == '__main__':
	print(main(1000)) # 31875000
