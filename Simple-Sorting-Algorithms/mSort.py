import tools
length = 1024
mini = 0
maxi = 9
Array = tools.randomArray(length, mini, maxi)
ArrayX = []
while len(Array) > 0:
	ArrayX.append([Array[0]])
	del Array[0]
def merge(array1, array2):
	temp = []
	appen = 0
	while appen < (len(array2) + len(array1)):
		temp.append(" ")
		appen += 1
	i = 1
	unfinished = True
	while unfinished:
		if len(array1) == 0:
			while len(array2) > 0:
				temp[-i] = array2[-1]
				del array2[-1]
				i += 1
			unfinished = False
		if len(array2) == 0:
			while len(array1) > 0:
				temp[-i] = array1[-1]
				del array1[-1]
				i += 1
			unfinished = False

		if unfinished:
			if array2[-1] == array1[-1]:
				temp[-i] = array2[-1]
				i += 1
				temp[-i] = array1[-1]
				i += 1
				del array2[-1]
				del array1[-1]
			elif array1[-1] > array2[-1]:
				temp[-i] = array1[-1]
				i += 1
				del array1[-1]
			elif array2[-1] > array1[-1]:
				temp[-i] = array2[-1]
				i += 1
				del array2[-1]

	place = 0
	while (len(temp) == place) == False:
		array1.append(temp[place])
		place += 1
	del array2


i = 0
while len(ArrayX) > 1:
	if i + 2  > len(ArrayX):
		i = 0
	merge(ArrayX[i], ArrayX[i+1])
	del ArrayX[i+1]
	i += 1



print(ArrayX[0])