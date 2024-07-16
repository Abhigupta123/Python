word = "sanu"

with open("sanu.txt") as f:
    content = f.read()

newcontent = content.replace(word , "Abhishek")

with open("sanu.txt","w") as f:
    f.write(newcontent)