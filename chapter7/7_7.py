startHour = int(input("Please input the start hour: "))
startMinute = int(input("Please input the start minute: "))
endingHour = int(input("Please input the ending hour: "))
endingMinute = int(input("Please input the ending minute: "))
if (endingHour>21):
  
  hour = 21 - startHour
  minute = (0 - startMinute) / 60
  hour = hour + minute
  wage = hour * 2.5

  sleepHour = endingHour - 21
  sleepMinute = endingMinute / 60
  sleepHour = sleepHour + sleepMinute
  wage += sleepHour * 1.75

else:
  hour = endingHour - startHour
  minute = (endingMinute - startMinute) / 60
  hour = hour + minute
  wage = hour * 2.5

print("The wage is ", wage)