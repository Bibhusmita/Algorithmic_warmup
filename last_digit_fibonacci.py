# Uses python3


def last_digit_fibonacci(n):
	if(n<=1):
		c = n
	a, b= 0,1
	for i in range(n-1):
		c = a + b
		c = c%10
		a, b = b, c
	return c

n = int(input())
print(last_digit_fibonacci(n))

