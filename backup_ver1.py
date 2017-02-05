import os
import time 


# Specify source of file and directories to be backed up
source = ['/Desktop/funny']

# Specify the target directory of the back-up
target_dir = ['/Desktop/backup']

# The name of the zip archive is the current date and time
target = target_dir + os.sep + \
	     time.strftime('%Y%m%d%H%M%S') + '.zip'

# Create target directory if not preset
if not os.path.exists(target_dir):
	os.mkdir(target_dir) # craete the directory

