import getpass
import os
import sys
import shutil

def copy_walls(target_dir):
	current_user = getpass.getuser()
	win_content_deliverydir = ""
	win_packages_dir = os.environ['SYSTEMDRIVE'] + "\\Users\\" + current_user + "\\AppData\\Local\\Packages\\"
	files = [f for f in os.listdir(win_packages_dir) if os.path.isdir(win_packages_dir + f)]
	for file in files:
		if "Microsoft.Windows.ContentDeliveryManager" in file:
			win_content_delivery_dir = file
	win_spotlight_dir = win_packages_dir + win_content_delivery_dir + "\\LocalState\\Assets\\"
	walls = [ f for f in os.listdir(win_spotlight_dir) if os.path.isfile( win_spotlight_dir + f)]
	for file in walls:
		if os.stat(win_spotlight_dir + file).st_size >= 200000:
			shutil.copy2(win_spotlight_dir + file , target_dir + file + ".jpg")
			print "copied " + win_spotlight_dir + file + " to " + target_dir + file + ".jpg"

def usage():
	print "Usage : ./{} Target_Directory_name".format(sys.argv[0])
	exit()

def main():
	if len(sys.argv) != 2:
		usage()
	if not os.path.isdir(sys.argv[1]):
		print "Please pass a valid directory...\n\n"
		usage()
	copy_walls(os.getcwd() + "\\" + sys.argv[1] + "\\")	

main()
