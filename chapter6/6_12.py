def sumList(nums):
	sumL = 0
	for i in range(0,len(nums)):
		sumL += nums[i]
	return sumL

nums = [2,4,76,98,5,3,2,4]
print(sumList(nums))
