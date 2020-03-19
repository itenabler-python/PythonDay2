import os

# for folderNameT, subfoldersT, filenamesT in os.walk("d:\\Pythontest\\Day 2"):
#     # print('The current folder is:' + folderNameT)
#
#     # for S in subfoldersT:
#     #     print('SUBFOLDER OF' + folderNameT + ': ' + S)
#
#     for T in filenamesT:
#         print('FILE INSIDE ' + folderNameT + ": " + T)

print(os.getcwd())

for file in os.listdir():
    # print(file)
    templist = file.rsplit(".",1)
    if len(templist) > 1:
        print(templist[0])