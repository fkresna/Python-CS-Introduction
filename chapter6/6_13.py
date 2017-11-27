def toNumbers(strList):
	for i in range(0,len(strList)):
		strList[i] = int(strList[i])
	return strList

strList = ['1','2','3']
print(toNumbers(strList))
