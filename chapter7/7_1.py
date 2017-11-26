hours = int(input("Please input the hours "))
rate = int(input("Please input the hourly rate "))
wage = 0
if (hours>40):
  wage = 40 * rate
  wage += 1.5 * rate * (hours-40)
else:
  wage = hours * rate
print("Total wage for the week: ",wage)