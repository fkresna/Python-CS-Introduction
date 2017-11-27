def print_song(activity,num):
	lyrics = "The ants go marching "+num+" by "+num+", hurrah! hurrah!\n"
	lyrics += lyrics
	lyrics += "The ants fo marching "+num+" by "+num+", \n"
	lyrics += "The "+activity+" stops to suck his thumb,\n"
	lyrics += "And they all go marching down...\n"
	lyrics += "In the ground...\n"
	lyrics += "To get out...\n"
	lyrics += "Of the rain.\n"
	lyrics += "Boom! Boom! Boom!\n"
	return lyrics

for i in range(1,11):
	if(i == 1):
		num = "one"
	elif(i==2):
		num = "two"
	elif(i==3):
		num = "three"
	elif(i==4):
		num="four"
	elif(i==5):
		num="five"
	elif(i==6):
		num="six"
	elif(i==7):
		num="seven"
	elif(i==8):
		num = "eight"
	elif(i==9):
		num = "nine"
	elif(i==10):
		num="ten"
	print(print_song("little one",num))

