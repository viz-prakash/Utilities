import getpass
import os
import sys
import shutil
import imghdr
from PIL import Image

# copy the script to target Directory and run the script with target directory as .
# or give path to target directory relative to your current directory

def copy_walls(target_dir):
	current_user = getpass.getuser()
	if not os.path.isdir(target_dir):
		os.makedirs(target_dir )
	tablet_target_dir = target_dir + "\\Tablet\\"
	win_content_deliverydir = ""
	win_packages_dir = os.environ['SYSTEMDRIVE'] + "\\Users\\" + current_user + "\\AppData\\Local\\Packages\\"
	files = [f for f in os.listdir(win_packages_dir) if os.path.isdir(win_packages_dir + f)]
	for file in files:
		if "Microsoft.Windows.ContentDeliveryManager" in file:
			win_content_delivery_dir = file
	win_spotlight_dir = win_packages_dir + win_content_delivery_dir + "\\LocalState\\Assets\\"
	walls = [ f for f in os.listdir(win_spotlight_dir) if os.path.isfile( win_spotlight_dir + f) ]
	for file in walls:
		format = imghdr.what(win_spotlight_dir + file)
		if os.stat(win_spotlight_dir + file).st_size < 200000 :
			print "not copying {} because size is less than 200000 bytes".format(win_spotlight_dir + file)
		elif format is None :
			print "not copying {} because couldn't figure out the image format of file".format(win_spotlight_dir + file)
		elif os.path.isfile(target_dir + file + "." + format) :
			print "not copying {} because file with same name and same image format already exist in target directory".format(win_spotlight_dir + file)
		else:	
			im = Image.open(win_spotlight_dir + file)
			width = im.size[0]
			height = im.size[1]
			if width < height:
				if not os.path.isdir(tablet_target_dir):
					os.makedirs(tablet_target_dir)
				shutil.copy2(win_spotlight_dir + file , tablet_target_dir + file + "." + format)
				print "copied " + win_spotlight_dir + file + " to " + tablet_target_dir + file + "." + format
			else:
				shutil.copy2(win_spotlight_dir + file , target_dir + file + "." + format)
				print "copied " + win_spotlight_dir + file + " to " + target_dir + file + "." + format

def usage():
	print "Usage : ./{} Target_Directory_Name".format(sys.argv[0])
	print "\n This script copies Spotlight wallpaper on Windows 10 to you desired directory"
	print "\n\n\t\tcopy the script to target Directory and run the script with target directory as ."
	print "\n\t\t or give path to target directory relative to your current directory"
	exit()

def main():
	if len(sys.argv) != 2:
		usage()
	'''
	if not os.path.isdir(sys.argv[1]):
		print "Please pass a valid directory...\n\n"
		usage()
	'''
	copy_walls( sys.argv[1] + "\\")	

main()
