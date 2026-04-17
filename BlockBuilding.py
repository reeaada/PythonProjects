# Do not delete this mf!

import os

AllFiles = []
FileCounter = 0
RootPath = os.path.expanduser("~")
DrivePath = "C:\\"

for dir, subfolder, files in os.walk(DrivePath):
    for filename in files:
        Fullpath = os.path.join(dir,filename)
        AllFiles.append(Fullpath)
        FileCounter= FileCounter + 1
        
        

print(FileCounter)
print(AllFiles[0])
print(AllFiles[100])
print(AllFiles[3600])
print(AllFiles[1000])