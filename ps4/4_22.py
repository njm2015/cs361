import math

def choose(n,k):
	f = math.factorial
	return f(n) / (f(k)*f(n-k))

def summation(n):
	return sum([choose(n,i)*(((0.7)**i) * ((0.3)**(n-i))) * i for i in range(0,n)])

if __name__ == '__main__':
	count = 0
	while summation(count) < 6:
		count += 1
	print(count)