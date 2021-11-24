import sys
import time

if len(sys.argv) == 2:
	FILEDIR = sys.argv[1]
else:
	FILEDIR = input("Enter File: ")

FILE = open(FILEDIR, "r")

CODE = FILE.readlines()
CODE_ARRAY = []
for y in range(len(CODE)):
	CODE[y] = CODE[y].replace("\n"," ")
	test = []
	for x in CODE[y]:
		test.append(x)
	CODE_ARRAY.append(test)

class Compiler():
	def __init__(self,code):
		self.stack = []
		self.CODE = code
		self.dot = 0
		self.pos = [0,0]
	def output(self,text):
		print(text)
	def nextln(self):
		self.pos = [self.pos[0] + 1, 0]
		self.main()
	def check(self,ifnt):
		if self.dot == ifnt:
			self.nextln()
	def add(self):
		self.dot += 1
	def minus(self):
		self.dot -= 1
	def sadd(self):
		self.stack.append(self.dot)
		self.dot = 0
	def sminus(self):
		self.dot = self.stack[len(self.stack) - 1]
		self.stack.remove(self.stack[len(self.stack) - 1])
	def i(self):
		self.dot = int(input("Input Number"))
	def main(self):
		code = self.CODE
		instr = False
		instrc = ""
		mem = ""
		for i in code[self.pos[0]]:
			if instr:
				if not(code[self.pos[0]][self.pos[1]] == '"') or mem == "":
					if not(mem == ""):
						if mem == "a":
							mem = ""
						mem += code[self.pos[0]][self.pos[1]]
					else:
						mem += "a"
				else:
					instr = False
					if instrc == "o":
						self.output(mem)
						mem = ""
					elif instrc == "i":
						try:
							if int(mem) == self.dot:
								self.nextln()
								break
							mem = ""
						except:
							print(f"Error at {self.pos} arg needs to be number not {mem}")
							exit()
					elif instrc == "l":
						try:
							if int(mem) == self.dot:
								self.nextln()
								break
							else:
								self.pos = [self.pos[0],0]
								self.main()
								break
							mem = ""
						except:
							print(f"Error at {self.pos} arg needs to be number not {mem}")
							exit()
			elif code[self.pos[0]][self.pos[1]] == "$" and code[self.pos[0]][self.pos[1] + 1] == '"':
				instr = True
				instrc = "o"
			elif code[self.pos[0]][self.pos[1]] == "\\" and code[self.pos[0]][self.pos[1] + 1] == 'n':
				self.nextln()
				break
			elif code[self.pos[0]][self.pos[1]] == "?" and code[self.pos[0]][self.pos[1] + 1] == '"':
				instr = True
				instrc = "i"
			elif code[self.pos[0]][self.pos[1]] == "l" and code[self.pos[0]][self.pos[1] + 1] == '"':
				instr = True
				instrc = "l"
			elif code[self.pos[0]][self.pos[1]] == "+" and code[self.pos[0]][self.pos[1] + 1] == '+':
				self.sadd()
			elif code[self.pos[0]][self.pos[1]] == "-" and code[self.pos[0]][self.pos[1] + 1] == '-':
				self.sminus()
			elif code[self.pos[0]][self.pos[1]] == "+" and code[self.pos[0]][self.pos[1] + 1] == ' ' and code[self.pos[0]][self.pos[1] - 1] == ' ':
				self.add()
			elif code[self.pos[0]][self.pos[1]] == "-" and code[self.pos[0]][self.pos[1] + 1] == ' ' and code[self.pos[0]][self.pos[1] - 1] == ' ':
				self.minus()
			elif code[self.pos[0]][self.pos[1]] == "i" and code[self.pos[0]][self.pos[1] + 1] == ' ' and code[self.pos[0]][self.pos[1] - 1] == ' ':
				self.i()
			self.pos = [self.pos[0],self.pos[1] + 1]


comp = Compiler(CODE_ARRAY)
comp.main()

time.sleep(10)

FILE.close()
