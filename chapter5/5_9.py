def main():
  print("This program calculates the number of words in a sentence")
  p = input("Enter a sentence: ")
  words = p.split()
  wordCount = len(words)
  print("The total word count is:", wordCount)

main()