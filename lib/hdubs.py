#-*-coding: utf-8-*-
from math import sqrt as r
PI = 3.14159265359
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

def divisors(num):
	d = []
	for n in range(2,int(num/2)+1):
		if num%n == 0:
			d.append(n)
	return d

def factors(num):
	f = []
	for n in range(2, int(num/2)+1):
		if num%n == 0:
			f.append((n,int(num/n)))
	return f

def isrightangle(a,b,c):
	if hyp(a,b) == c:
		return True
	return False

special45 = lambda h: h/r(2)
special30 = lambda b: b/r(3) 

def sqrtWIP(num):
	for n in range(2,int(num/2)):
		if n*n == num:
			return n
	return -1

def commonDividers(*numbers):
	goto = int(min(numbers)) 
	dividers = []
	for div in range(2,goto+1):
		count = 0
		for n in numbers:
			if n%div == 0:
				count += 1
			else:
				break
		if count == len(numbers):
			dividers.append(div)
	if len(dividers) == 0:
		return [1] 
	return dividers

def simplify(num,den):
	divisor = 0
	while divisor != 1:
		divisor = min(commonDividers(num,den))
		num = int(num/divisor)
		den = int(den/divisor)
	return (num,den)

def getHyp(leg1, leg2):
	pleg1 = leg1**2
	pleg2 = leg2**2
	hyp = r(pleg1+pleg2)
	if hyp <= leg1 or hyp <= leg2:
		return -1
	return hyp

def getLeg(hyp, leg): 
	if hyp <= leg:
		return -1
	hyp **= 2
	nleg = hyp - leg**2

	return r(nleg)	

def mcm(n1, n2, top=10, all=False):
	n1l = []
	n2l = []
	for n in range(1,top+1):
		n1l.append(n1*n)
		n2l.append(n2*n)
	for n in n1l:
		if n in n2l:
			if not all:
				return n
			else: 
				return (n, int(n/n1), int(n/n2))		
	return -1
#Volume.
cubeVolume = lambda l: l**3	
rectangularPrsmVolume = lambda h,b,p: p*(h*b)
trianglePrsmVolume = lambda h,b,p: p*((h*b)/2)
triangleArea = lambda h,b: (h*b)/2
sqrArea = lambda l: l*4
rectangleArea = lambda h,b: h*b
circleArea = lambda r: PI*(r**2)
semiCircleArea = lambda r: (PI*(r**2))/2
