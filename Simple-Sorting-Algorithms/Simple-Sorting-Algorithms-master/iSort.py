import tools
length = 1024
mini = 0
maxi = 9
Array = tools.randomArray(length, mini, maxi)
#Array = [6, 4, 6, 7, 5]
def iSort(array):
	Sorted = []
	unsorted = array
	Sorted.append(unsorted[-1])
	del unsorted[-1]
	running = True
	while running:
		if len(unsorted) > 0:
			Sorted.append(unsorted[-1])
			del unsorted[-1]
		i = 0
		bubbling = True
		running = False
		while bubbling:
			i += 1
			if i+1 > len(Sorted):
				i -= 1
			if Sorted[-i] < Sorted[-i - 1]:
				temp = Sorted[-i]
				Sorted[-i] = Sorted[-i - 1]
				Sorted[-i - 1] = temp 
				running = True
			else:
				bubbling = False
		if len(unsorted) > 0:
			running = True
	print(Sorted)
iSort(Array)
