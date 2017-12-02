import math

def areaPizza(d):
	r = d/2
	A= 4 * math.pi*r**2
	return A

def cost(price,d):
	A = areaPizza(d)
	c = price / A
	return c
d = eval(input("Please input the pizza diameter"))
price = eval(input("Please input the pizza prize"))
print(areaPizza(d))
print(cost(price,d))
