# Ver.1.31 Update Notes
# Added notifier if file is incomplete
print("vinfo v1.31")
import os
import sys
if(not len(os.popen("mediainfo --help").read().split("\n", 5)) is 6):
	print("Dependency 'mediainfo' is not installed")
	sys.exit()
		
ls = os.popen("ls").read().split("\n")
vidForms = ".mp4 .mkv .flv"  
longest = 0
files = []
vids = []
termOuts = []
space = "                   "

# formats name for command ussage
def nameFormat(name):
	out = "File " + name + " has single quotoes, double quotes, and spaces. Therefore it can not run through this program"
	if("'" in name and '"' in name):
		print(out)
	else:
		if("'" in name):
			return '"' + name + '"'
		else:
			return "'" + name + "'"


def FullSearch(IN):
	OUT = []
	i = 0
	while(i < len(IN)):
		if("'" in IN[i]):
			termOut = os.popen('mediainfo "' + IN[i] + '"').read()
		else:
			termOut = os.popen("mediainfo '" + IN[i] + "'").read()
		if("\nVideo\n" in termOut):
			OUT.append(IN[i])
			termOuts.append(termOut)
		i += 1
	return OUT

def TagSearch(IN):
	OUT = []
	i = 0
	while(i < len(IN)):
		if('.' in IN[i]):
			tag = IN[i].split(".")[-1]
			if(tag in vidForms):
				OUT.append(IN[i])
		i += 1
	return OUT

i = 0
while(i < len(ls)):
	if(os.path.isfile(ls[i])):
		files.append(ls[i])
	i += 1
		
vids = TagSearch(files)
#vids = FullSearch(files)

if(len(termOuts) > 0):
	termsLogged = True
else:
	termsLogged = False

i = 0
while(i < len(vids)):
	if(len(vids[i]) > longest):
		longest = len(vids[i])
	i += 1

i = 0
while(i < len(vids)):
	if(termsLogged):
		sleep(.5)
		termOut = termOuts[i]
	else:
		termOut = os.popen("mediainfo " + nameFormat(vids[i])).read()
	try:
		tempo = termOut.split("Duration", 1)[1].split(":", 1)[1].split("\n", 1)[0]
		temp = termOut.split(" pixels", 3)
		width = temp[0].split("Width",1)[1].split(": ")[1]
		height = temp[1].split("Height",1)[1].split(": ")[1]
		complete = ""
		if("IsTruncated" in termOut):
			complete = "\033[91m\033[1m  Incomplete\033[0m"
		if(longest < 20):
			print(vids[i] + ": " + space[0:longest - len(vids[i])] + width + ", " + height + " | " + tempo +  complete)
		else:
			print(vids[i] + ":\n" + width + ", " + height + " | " + tempo + complete + "\n")
	except:
		pass
	i += 1
