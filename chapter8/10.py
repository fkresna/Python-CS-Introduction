infile = open("10.txt","r")
count = 0
miles = []
mpg = []
for line in infile.readlines():
  if(count == 0):
    initOdometer = int(line)
    o1 = initOdometer

  elif (count == 1):
    legsInformation = line
  else:
    userInput = line
    if(userInput != ""):
      o,g = userInput.split()
      diffOdometer =  int(o) - int(o1) 
      o1 = o
      miles.append(diffOdometer)
      mpg.append(round(diffOdometer/float(g),2))
  count += 1
infile.close()
if (count >0):
  print(legsInformation)
  for i in range(0,len(miles)):
    print(miles[i] , " " ,mpg[i]," mpg")