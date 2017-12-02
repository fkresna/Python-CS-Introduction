def main():
  pos = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  name = "John Marvin Zelle"
  sum = 0
  temp = 0
  for ch in name:
    temp = pos.find(ch) 
    print(temp," ")
    sum = sum + temp
  print("sum: " + str(sum))
main()