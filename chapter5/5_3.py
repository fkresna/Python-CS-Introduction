def main():
  score = int(input("Please input the score"))
  grade =  ["F","F","F","F","F","F","F","F","F","F"]
  grade.extend(["F","F","F","F","F","F","F","F","F","F"])
  grade.extend(["F","F","F","F","F","F","F","F","F","F"])
  grade.extend(["F","F","F","F","F","F","F","F","F","F"])
  grade.extend(["F","F","F","F","F","F","F","F","F","F"])
  grade.extend(["F","F","F","F","F","F","F","F","F","F"])
  grade.extend(["D","D","D","D","D","D","D","D","D","D"])
  grade.extend(["C","C","C","C","C","C","C","C","C","C"])
  grade.extend(["B","B","B","B","B","B","B","B","B","B"])
  grade.extend(["A","A","A","A","A","A","A","A","A","A"])
  print(grade[score])
main()