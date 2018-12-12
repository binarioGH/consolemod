#-*-coding: utf-8-*-
from socket import *
class Client():
	def __init__(self, ip="127.0.0.1", port=5000):
			self.__sock = socket(AF_INET)
			self.__sock.connect((ip, port))
			self.hearing = True
	def printrecv(self):
		while self.hearing:
			try:
				msj = self.__sock.recv(1024).decode()
				print(msj)
			except:
				pass
	def send(self, msj):
		msj = str(msj).encode()
		self.__sock.send(msj)
