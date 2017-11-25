initial = 1
interest = 0.1
interest2 = interest*100
endBalance = initial
count = 0
while (endBalance < initial*2):
  endBalance = endBalance + endBalance * interest 
  count += 1

print(str(count) + " years to get $" + str(round(endBalance,2)) + " from $" + str(initial) + " with " + str(interest2) + "%")