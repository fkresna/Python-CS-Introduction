def sumN(n):
	sum1 = 0
	for i in range(0,n):
		sum1 += i
	return sum1

def sumNCubes(n):
	sumCubes = 0
	for i in range(0,n):
		sumCubes += i**3
	return sumCubes

n = int(input("Please input n"))
print(sumN(n))
print(sumNCubes(n))
