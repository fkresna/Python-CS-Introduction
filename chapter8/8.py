inputM = int(input("Please input m "))
inputN = int(input("Please input n "))
n = inputN
m = inputM
while(m>0):
  temp = n
  n = m
  m = temp%m

print("GCD between " +str(inputM) + " and " + str(inputN) +" is " + str(n))