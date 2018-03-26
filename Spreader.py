import os

directory_to_check = input("Dir: ") # Which directory do you want to start with?

def my_function(directory):
	print("Listing: " + directory)
	print("\t-" + "\n\t-".join(os.listdir("."))) # List current working directory

# Get all the subdirectories of directory_to_check recursively and store them in a list:
directories = [os.path.abspath(x[0]) for x in os.walk(directory_to_check)]
#directories.remove(os.path.abspath(directory_to_check)) # If you don't want your main directory included
Script = input("Command: ")
for i in directories:
	if(".ignore" not in i):
		os.chdir(i)         # Change working Directory
		os.system(Script)      # Run your function