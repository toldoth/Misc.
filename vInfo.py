import os
import sys
if(not len(os.popen("mediainfo --help").read().split("\n", 5)) is 6):
	sys.exit()
  
vids = os.popen("ls").read().split("\n")
i = 0
while(i < len(vids)):
	if("'" in vids[i]):
		termOut = os.popen('mediainfo "' + vids[i] + '"').read()
	else:
		termOut = os.popen("mediainfo '" + vids[i] + "'").read()
	if("\nVideo\n" in termOut):
		tempo = "tempo"
		tempo = termOut.split("Duration", 1)[1].split(":", 1)[1].split("\n", 1)[0]
		temp = termOut.split(" pixels", 3)
		Temp = temp[0].split("Width",1)[1].split(": ")[1]
		TEmp = temp[1].split("Height",1)[1].split(": ")[1]
		print(vids[i] + ":\n" + Temp + ", " + TEmp + " | " + tempo + "\n")
	i += 1
