avg = eval(input(:Please input average temperature))
heating = []
cooling = []
if (avg < 60):
  heating.append(avg)
elif (avg>80):
  cooling.append(avg)