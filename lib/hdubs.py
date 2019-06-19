#-*-coding: utf-8-*-
from math import sqrt as r
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

def interiorAngles(n):
	return (n-2)*180

def sumExteriorAngles(n):
	return 360

def eachAngle(n):
	return ((n-2) * 180 )/n

def eachExteriorAngle(n):
	return 360/n

def angleTable(*angles):
	info = {}
	for angle in angles:
		info[str(angle)] = {"Interior Angle Sum": interiorAngles(angle),
		"Each Interior Angle": eachAngle(angle),
		"Exterior Angle Sum": 360,
		"Each Exterior Angle": eachExteriorAngle(angle)}
	return info
def displayAngleTable(info):
	for angle in info:
		print("-"*80)
		for i in info[angle]:
			print("{} : {}".format(i, info[angle][i]))

def average(*nums):
	total = 0
	for num in nums:
		total += num
	return total / len(nums)

def distanceformula(x1, y1, x2, y2):
	return r((x2 - x1)**2 + (y2 - y1)**2)