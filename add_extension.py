import os
import sys

def add_extension(directory, extension):
	files = [ f for f in os.listdir(directory) if os.path.isfile(f)]
	for file in files:
		if "." not in file: 
			if "." not in extension:
				print "renaming " + file + " to " + file + "." + extension
				os.rename(file, file + "." + extension)
			else: 
				print "renaming " + file + " to " + file + extension
				os.rename(file, file + extension)

def usage():
	print "Adds passed extension to the files in given directory which already doesn't have an extension"
	print "Usage : ./{} Directory_name Extenstion_to_add".format(sys.argv[0])
	exit()
		
def main():
	if len(sys.argv) != 3:
		usage()
	if os.path.isfile(sys.argv[1]):
		print "Please pass a valid directory...\n\n"
		usage()
	add_extension(sys.argv[1], sys.argv[2])

main()	
