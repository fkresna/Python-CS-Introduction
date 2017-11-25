
print("Wind \t | Temperature \t | Windchill Index")
for v in range(0,51,5):
  for t in range(-20,61,10):
    if (v>3) :
      wi = 35.74 + 0.6215 * t - 35.75 * (v**0.16) + 0.4275 * t * (v**0.16)
      print(str(v) + "\t | " + str(t) + "\t\t | " + str(wi));
    else:
      print(str(v) + "\t | " + str(t) + "\t\t | 0");