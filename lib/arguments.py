#-*-coding: utf-8-*-
class Parser():
	def __init__(self):
		self.options = {}
	def addOption(self, option):
		self.options[option] = None
	def parse(self, args):	
		count = 0
		for a in args:
			if str(a)[0] != "-":
				count += 1
				continue
			else: 
				if a in self.options:
					self.options[a] = args[count + 1]