#-*-coding: utf-8-*-
from socket import * 
class Chat():
	def __init__(self, ip="127.0.0.1", port=5000, l=1):
		self.lcant = l
		self.__sock = socket(AF_INET)
		self.__sock.bind((ip, port))
		self.__sock.listen(self.lcant)
		self.__sock.settimeout(0.0)
		self.clients = []
		self.door = True
		self.ears = True
		self.printaddrs = False
	def searchconn(self):
		while self.door:
			while len(self.clients) <= self.lcant:
				try:
					conn, addr = self.__sock.accept()
					self.clients.append(conn)
					if self.printaddrs:
						print(addr)
				except:
					pass
	def hearing(self):
		while self.ears:
			for c in self.clients:
				try:
					msj = c.recv(1024)
				except:
					pass
				else:
					self.sendtoall(msj, c)
	def sendtoall(self,msj, messenger=None):
		for client in self.clients:
			try:
				if client == messenger:
					continue
				else:
					client.send(msj)
			except:
				self.clients.remove(client)