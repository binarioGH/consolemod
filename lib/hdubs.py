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

def idk(a,b):
	"This is useful for midpoint formula function."
	return (a+b)/2

def midpointformula(x1, y1, x2, y2):
	return (idk(x1, x2), idk(y1, y2))

def slope(x1, y1, x2, y2):
	return y2 - y1 / x2 - x1

def simplify(n1,n2, m="undefined"):
	count = 2
	if m == "undefined":
		m = min(n1,n2)
	while count <= int(m/2):
		if n1%count == 0 and n2%count == 0:
			n1 = int(n1/count)
			n2 = int(n2/count)
		else:
			count += 1
	return (n1, n2)
def ratio(n1, n2):
	n1, n2 = simplify(min(n1,n2), max(n1,n2))
	return "{}:{}".format(n1, n2)

sqrtperimeter = lambda s: l*4
equilateraltriangleper = lambda s: l*3
isoscelestriangleper = lambda s, b: s*2 + b
rectangleper = lambda b, s: b*2 + s*2
pentagonper = lambda s: s*5
hexagonper = lambda s: s*6
heptagon = lambda s: s*7
octagon = lambda s: s*8

def hyp(a,b):
	a **=2
	b **=2
	a += b
	return r(a)
def leg(h,l):
	h **=2
	l **=2
	h -= l
	h = absval(h)
	h = r(h)
	if h%1 != 0:
		return h
	return int(h)