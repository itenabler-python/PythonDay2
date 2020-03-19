
import shutil
import os
from send2trash import *

# remove the whole direc
path = os.getcwd()
if os.path.isdir(path + "folder2_backup") is True:
    shutil.rmtree(path + "folder2_backup")

#Permanent deleted cannot recover from recycle bin
# os.unlink(path + "/folder2/newfolder/newhelloworld.txt")

#Delete to recycle bin
send2trash("helloworld.txt")

