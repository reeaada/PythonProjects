import re

Password = input("Enter a passowrd : ")
Score = 0
Failures = []

if len(Password) >= 8:
    Score += 1
else:
    Failures.append("At least 8 characters")

if re.search(r"[A-Z]",Password):
    Score += 1
else:
    Failures.append("At least one upper character")
    
if re.search(r"[a-z]", Password):
    Score += 1
else:
    Failures.append("At least one lower character")
    
if re.search(r"[0-9]",Password):
    Score += 1
else:
    Failures.append("At least one number")

if re.search(r"[!@#$%^&*(),.?]", Password):
    Score += 1
else:
    Failures.append("At least one symbol")
    
if Score <= 2 :
    print("your pass is weak")
elif Score == 3:
    print("your password is medium")
elif Score == 4:
    print("your password is strong")
else:
    print("your password is very strong")
    
print("Your failueres : ")
print("====================================")

for i in Failures:
    print(i)
    
    
