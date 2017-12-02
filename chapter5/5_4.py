def main():
  userInput = input("Please input words ")
  inputs = userInput.split()
  text = ""
  for i in range(0,len(inputs)):
    text += inputs[i][0].upper()
  print(text)
main()