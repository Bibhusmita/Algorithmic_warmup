# Uses python3

import sys
def fib_again(n,m):
	if(n<=1):
		return (n%m)

	a, b = 0, 1
	for i in range(n-1):
		c = a+b
		a, b = b, c

	return (c%m)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(fib_again(n,m))
