#-*-coding: utf-8
from subprocess import run, PIPE
from sys import argv
from optparse import OptionParser as opt

def compile(name, outname=0):
	compiler = "C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319\\csc.exe"
	if outname:
		out = " -out:{} ".format(outname)
	else:
		out = " "
	execute = run("{}{}{}".format(compiler, out, name), shell=True, stdout=PIPE, stderr=PIPE)
	output = "{}{}".format(execute.stdout.decode("latin1"), execute.stderr.decode("latin1"))
	print(output)
def main():
	op = opt("Usage: %prog [options] [values]")
	op.add_option("-o", "--out", dest="out", default=0, help="Define out file's name.")
	op.add_option("-f", "--file", dest="file", default=0, help="Input the name of the C# file that you want to compile.")
	(o, argv) = op.parse_args()
	if not o.file:
		print("You didn't specified the file that you want to compile.")
		exit()
	compile(o.file, o.out)

if __name__ == '__main__':
	main()