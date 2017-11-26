score = int(input("Please input quiz score "))
grade = 'F'
if(score == 5):
  grade = 'A'
elif (score == 4):
  grade = 'B'
elif (score == 3):
  grade = 'C'
elif (score == 2):
  grade = 'D'
elif (score == 1 or score == 0):
  grade = 'F'
print("The grade is ", grade)