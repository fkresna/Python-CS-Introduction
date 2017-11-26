speedLimit = eval(input("Please input the speed limit: "))
clockedSpeed = eval(input("Please input the clocked speed: "))
if(clockedSpeed > speedLimit):
  if(clockedSpeed < 90):
    fine = 50 + 5 * (clockedSpeed - speedLimit)
  else:
    fine = 50 + 5 * (clockedSpeed - speedLimit) + 200
else:
  fine = 0

if(fine == 0):
  print("The speed was legal")
else:
  print("The speed was illegal, Fine: ",fine)