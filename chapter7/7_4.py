numCredits = int(input("Please enter number of credits"))
classStanding = ""
if(numCredits < 7)
  classStanding = "Freshman"
elif (numCredits >=7 and numCredits <16)
  classStanding = "Sophomore"
elif (numCredits >=16 and numCredits <26)
  classStanding = "Junior"
elif (numCredits >= 26)
  classStanding = "Senior"

print("Class Standing: ",classStanding)