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

