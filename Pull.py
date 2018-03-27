import os
import shutil
def pull(File, output, skip):
	if(os.path.isdir(output) is False):
		os.makedirs(output)
	root = open(File, "r")
	raw = root.read()
	run = True
	spot = 0
	i = 0
	while(run):
		loc = raw.find("<img src", spot)
		if(loc is -1):
			run = False
		else:
			if(i > skip):	
				if(raw[loc+10:loc+140].split('"')[0][0] is "/"):
					shutil.copyfile(raw[loc+11:loc+140].split('"')[0], output + "/" + str(i))
				elif(raw[loc+10:loc+140].split('"')[0][0] is "." and raw[loc+10:loc+140].split('"')[0][1] is "/"):	
					shutil.copyfile(raw[loc+12:loc+140].split('"')[0], output + "/" + str(i))
				else:
					shutil.copyfile(raw[loc+10:loc+140].split('"')[0], output + "/" + str(i))
			spot = loc + 1
			i += 1
			
	root.close()
print("enter the name of the html file(s) to pull from, put '/' between multiple files")
Input = input(">>>").split("/")
print("enter name of output folder")
folder = input(">>>")
print("enter # of how many images to skip")
skip = int(input(">>>"))


i = 0
while(i < len(Input)):
	pull(Input[0], folder, skip)
	i += 1
print("***COMPLETE***")