import os
import time 


# Specify source of file and directories to be backed up
source = ['/home/rawteech/Desktop/funny']

# Specify the target directory of the back-up
target_dir = '/home/rawteech/Desktop/backup'

# The name of the zip archive is the current date and time
target = target_dir + os.sep + \
	     time.strftime('%Y%m%d%H%M%S') + '.zip'

# Create target directory if not preset
if not os.path.exists(target_dir):
	os.mkdir(target_dir) # craete the directory

# Use the zip command to archive the files in a zip
zip_command = "zip -r {0} {1}". format(target, ' '.join(source))

# Run the backup
print "Zip command is: "
print zip_command
print "Running:"
if os.system(zip_command) == 0:
	print "Successful backup to ", target
else:
	print "Backup FAILED!"
