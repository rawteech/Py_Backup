import os
import time 


# Specify source of file and directories to be backed up
source = ['/home/rawteech/Desktop/funny']

# Specify the target directory of the back-up
target_dir = '/home/rawteech/Desktop/backup'

# Create target directory if not preset
if not os.path.exists(target_dir):
	os.mkdir(target_dir) # craete the directory

# make the current day the name of the sub-directory
today = target_dir + os.sep + time.strftime('%Y%m%d')
# make the current time the name of the zip file
now = time.strftime('%H%M%S')

# take comment from user and add to name of zip file
comment = raw_input('Enter a comment --> ')

# then set the name of the zip file
target = today + os.sep + now + '.zip'

# create sub-directory if not existing
if not os.path.exists(today):
	os.mkdir(today)
	print "Successfully created directory ", today

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
