class reverse: 
	#Write a program which can reverse a list.. (while preserving the order) 

	def reverseList(nums):
		#make another list 
		newArr = [] 
		#Loop backwards 
		for num in reversed(nums):
			newArr.append(num)
		return newArr

	print(reverseList([1,2,3,4,3]))