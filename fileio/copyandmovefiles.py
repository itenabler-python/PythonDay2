import shutil
import os

print(os.getcwd())
path = os.getcwd()
# os.mkdir(path + "/folder2")
#copy helloworld to subfolder "folder2"
# shutil.copy("helloworld.txt", "folder2")

#backup of the folder2
# shutil.copytree("folder2", "folder2_backup")

#move helloworld.txt to a sub-subfolder newfolder
if os.path.isfile(path + "/folder2/newfolder/helloworld.txt" ) is False:
    if os.path.isdir(path + "/folder2/newfolder") is False:
        os.mkdir(path + "/folder2/newfolder")
        shutil.move("folder2/helloworld.txt", "folder2/newfolder/")
    else:
        print("Folder already exists!")
else:
    print("File already exists!")

shutil.move("folder2/newfolder/helloworld.txt", "folder2/newfolder/newhelloworld.txt")