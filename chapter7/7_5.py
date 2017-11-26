weight = eval(input("Please input the weight (in pounds) "))
height = eval(input("Please input the height (in inches) "))

bmi = round(weight * 720 / height**2)
range = ""
if (bmi >= 19 and bmi <=25):
  range = "within"
elif (bmi < 19):
  range = "below"
elif (bmi >25):
  range = "above"

print("Your BMI is ",bmi,"you are "+ range + " the healthy range")