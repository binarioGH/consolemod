#-*-coding: utf-8-*-
from platform import python_version as pv, system as s
from os import chdir, getcwd, system

if __name__ == '__main__':
	if str(pv())[0] == "3":
		raw_input = input
	if str(s()) == "Windows":
		clear = "cls" 
	else:
		clear = "clear"
	cmd = " "
	state = "python"
	while cmd.lower() != "exit":
		cmd = raw_input("{}({})>".format(getcwd(), state))
		try:
			if cmd[:2].lower() == "cd":
				chdir(cmd[3:])
			elif cmd == clear:
				system(clear)
			elif cmd.lower() == "chstate":
				if state == "python":
					state = "cmd"
				else:
					state = "python"
			else:
				if state == "python":
					exec(cmd)
				else:
					system(cmd)


		except Exception as e:
			print(e)

	