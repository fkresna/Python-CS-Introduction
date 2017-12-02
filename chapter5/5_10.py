def main():
  p = input("Enter a sentence: ")
  words = p.split()
  sumOfWord = 0
  for word in words:
    sumOfWord = sumOfWord + len(word)
  average = sumOfWord / len(words)
  print("The average word length is :", average)

main()