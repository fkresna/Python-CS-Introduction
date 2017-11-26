age = int(input("Please enter age: "))
yearsCitizenship = int(input("Please enter years of citizenship"))
if (age>=30 and yearsCitizenship >=9):
  senator = True
else:
  senator = False

if (age >=25 and yearsCitizenship>=7):
  representative = True
else:
  representative = False

if(senator):
  print("You are eligible to become US Senator")
else:
  print("You are not eligible to become US Senator")

if(representative):
  print("You are eligible to become US Representative")
else:
  print("You are not eligible to become US Representative")