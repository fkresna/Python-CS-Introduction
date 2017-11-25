import math

n = int(input("Please input a number "))
for i in range(1,n+1):
  if i == 2:
    print("2 ")
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
        print(str(i))