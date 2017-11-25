n = int(input("Please input how many number do you want?"))
n1 = 1
n2 = 1
if (n == 1):
  print(n1)
elif(n==2):
  print(n2)
else:
  print(n1)
  print(n2)
  for i in range(2, n):
    temp = n2
    n2 = n2 + n1
    n1 = temp 
    print(n2)