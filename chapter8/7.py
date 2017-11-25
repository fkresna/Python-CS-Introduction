import math

n = int(input("Please input a number "))
prime = []
if (n%2 == 0):
  #prime list
  for i in range(1,n+1):
    if i == 2:
      prime.append(2)
    else:
      if (i >2):
        min = 2
        max = math.ceil(i**0.5)
        count = 0
        for j in range(min,max+1):
          if(i%j == 0):
            count += 1
            break
        if(count == 0):
          prime.append(i)

  for num1 in prime:
    for num2 in prime:
      if num1 + num2 == n:
        print(str(num1) + "+" + str(num2) + "=" + str(n))