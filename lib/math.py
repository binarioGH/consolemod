#-*-coding: utf-8-*-
def mult(*nums):
	#Multiplicaciones
	t = nums[0]

	
	for i in nums[1:]:
		t*= i
	return t

def absval(n):
	#Valor absuluto
	if n < 0:
		return n * -1
	else:
		return n
def rest(n1, n2):
	#Resta
	return n1 - n2
def sum(n1, n2):
	#suma
	return n1 + n2

def div(n1, n2):
	#division
	return n1 / n2

def higher(*nums, mx=True, lst=["none"]):
	try:
		ret = nums[0]
	except:
		try:
			if lst[0] == "none":
				return 0
			else:
				ret = lst[0]
				nums = lst
		except:
			return 0
	for num in nums:
		if mx:
			if num >= ret:
				ret = num
		else:
			if num <= ret:
				ret = num
	return ret

def lower(*n):
	return higher(lst=n, mx=False)


def middle(n1, n2):
	low = lower(n1, n2)
	mid = (higher(n1, n2) - low) / 2
	mid += low
	return mid