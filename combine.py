import os
files = listdir("labels")
text=""
for file in files:
    f = open("labels/" + file,"r")
    content = "./train_img/" + file[0:5] + ".jpg "
    str = f.read()
    content += str
    text += content
nf = open("train.txt","a")
nf.seek(0) 
nf.truncate()
nf.write(text)