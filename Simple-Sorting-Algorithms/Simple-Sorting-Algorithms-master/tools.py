#tools library for use between playing with different scripts

#creates a random array with the length(count) and minimum/maximum number for the random int(mini/maxi)
def randomArray(count, mini, maxi):
	import random
	i = 0
	temp = []
	while i < count:
		temp.append(random.randint(mini, maxi))
		i += 1
	#returns temp so it can be used with the outside array in an array = randArray(parameters) format
	return temp
#creates a "quant" number of skipLns for organizing output
def skipLn(quant):
	skipLn = 0
	while skipLn < quant:
		print()
		skipLn += 1
def repeat(char, freq):
	temp = ""
	i = 0
	while i < freq:
		temp += char
		i += 1
	print(temp)
def repeatC(char, freq):
	temp = ""
	i = 0
	while i < freq:
		temp += char
		i += 1
	print()
	print(temp)
	print()