#all comments will be directly above the subject of any given comment, unless stated otherwise
#simple bubble sort algorithium that moves greater numbers to the right
import tools
#maximum and minimum for random array function
maxNum = 9
minNum = 0
#var in control of the length of the random array, the comment on the same line is for prompting the user in the terminal
length = 1024#length = int(input("Length of Random Bubble Sort: "))

		

#Creating random array with function from tools.py with the variables we created at the begining
Array = tools.randomArray(length, minNum, maxNum)


#bSort bSort bSort bSort bSort bSort bSort bSort bSort bSort bSort bSort bSort bSort
def bSort(array):
	fin = False
	while not fin:
		i = 0
		fin = True
		while i < len(array) - 1:
 
			if array[i] > array[i + 1]: 
				temp = array[i] 
				array[i] = array[i + 1]
				array[i + 1] = temp
				#sets fin to false. since this is called for the whole array before the "while not fin     
				#loop checks it again" it is only set to false when there are numbers moved(when its not finished)
				fin = False
			i += 1
	print(array)

	
#tools.repeatC("+", 40)
#printing the array for comparision with the output of bSort()
#print(Array)
#spaces/separators for organizing output more neatly
#tools.repeatC("-", 40)
#bSort called with Array(which is filled with a random array) and has a loop within it to repeat until complete
bSort(Array)
#tools.repeatC("-", 40)
#printing the number of times numbers in the array were checked/moved(if the number to the right of it was smaller)
#print("It took " + str(passThroughs) + " checks/movements to complete this bubble sort")
#printing how many time bubble sort ran, looking through each number, until complete
#print("Bubble sort had to run "  + str(repeats) + " times to complete")
#tools.repeatC("+", 40)




