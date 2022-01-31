#write a program to open three files 1.txt , 2.txt and 3.txt. if any of the files are not present, a massage without exiting the program must be printed promoting the same
def readFile(filename):
	try:
		with open(filename,'r') as f:
			print(f.read())
	except FileNameFoundError:
			print(f"File {filename} is not found")
					
readFile("1.txt")
readFile("2.txt")
readFile("3.txt")			