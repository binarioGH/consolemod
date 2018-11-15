from time import sleep
from threading import *

class Chrone():
	def __init__(self):
		self.__check = False
		self.times = []
	def __counter(self):
		d = 0
		h = 0
		m = 0
		s = 0
		for t in range(0,10000):
			sleep(1)
			s += 1
			if s == 60:
				m += 1
				s = 0
				if m == 60:
					h += 1
					m = 0
					if h == 24:
						d += 1
						h = 0
			if self.__check == False: 
				self.times.append({"d":d,"h":h,"m":m,"s":s})
				return 0
			'''for d in range(0,365):
			       for h in range(0,24):
			           for m in range(0,60):
			               for s in range(0,60):
						       sleep(1)'''
	def start(self):
		self.__check = True
		chrone = Thread(target=self.__counter)
		chrone.daemon = True
		chrone.start()
	def stop(self):
		self.__check = False


		
