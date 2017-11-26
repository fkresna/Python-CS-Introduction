year = int(input("Please input year: "))
a = year % 19
b = year % 4
c = year%7
d = (19*a + 24)%30
e = (2*b + 4*c+6*d+5) %7
easter = 22 + d + e
if (easter > 31):
  easter = easter - 31
  print("The easter date is April", easter, year)
else:
  print("The easter date is March",easter)