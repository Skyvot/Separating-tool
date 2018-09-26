#created by Skyvot 2018-09-26

import os
f = open("train.txt","r")
str = f.read()
p = str.split("./train_img/")
if not os.path.exists("labels/"):
    os.mkdir("labels/")
for epic in p:
    if epic == "":
        continue
    filename = epic[0:5] + ".txt"
    pathname = "labels/" + filename
    print(pathname + " is in process...")
    text = epic[10:]
    # If you deal with a single picture for several times and you only need what you did in the last time, use this:
    nf = open(pathname,"a")
    nf.write(text)
    '''
    # If you deal with a single picture for several times and you want to keep what you did every single time, use this:
    if not os.path.exists(pathname):
        nf = open(pathname,"a")
        nf.write(text)
    else:
        nf = open(pathname,"a")
        nf.seek(0)
        nf.truncate()
        nf.write(text)
    '''
    print(pathname + " is done.")