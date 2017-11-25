initOdometer = int(input("Please input starting odometer reading "))
legsInformation = input("Please input information about a series of legs ")
o1 = initOdometer
miles = []
mpg = []
userInput = None
while(userInput != ""):
  userInput = str(input("Please input odometer reading and amount of gas used (separated by a space)"))
  if(userInput != ""):
    o,g = userInput.split()
    diffOdometer =  int(o) - int(o1) 
    o1 = o
    miles.append(diffOdometer)
    mpg.append(round(diffOdometer/float(g),2))

print(legsInformation)
for i in range(0,len(miles)):
  print(miles[i] , " " ,mpg[i]," mpg")