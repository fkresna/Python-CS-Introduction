import math

n = int(input("Please input a number "))
if (n >2):
  min = 2
  max = math.ceil(n**0.5)
  count = 0
  for i in range(min,max+1):
    if(n%i == 0):
      count += 1
  if(count ==0):
    print("Prime")
  else:
    print("Not Prime")