#-*-coding: utf-8-*-
from platform import python_version as pv

class Lector:
	def __init__(self, file):
		self.file = file
		

	def readall(self):
		with open(self.file, "r") as f:
			for line in f: 
				print(line)
	def countletter(self, letter):
		count = 0
		with open(self.file, "r") as f:
			for line in f:
				for char in line:
					if letter == char.lower():
						count += 1
		return count
'''	def addlines(self, breaker):
		add = " "
		with open(self.file, "w") as f:
			while add != breaker:
				add = raw_input("-")
				f.write(add)


if __name__ == '__main__':
	if str(pv()) == "3":
		raw_input = input'''