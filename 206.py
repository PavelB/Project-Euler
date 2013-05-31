import re

def main():
	prog = re.compile('1.2.3.4.5.6.7.8.9.0')
	n = 1000000000
	while prog.match(str(n * n)) == None:
		n += 10
	return n

if __name__ == '__main__':
	print(main()) # 1389019170
