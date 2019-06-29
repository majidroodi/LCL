#!/usr/bin/python3.7

import os
import sys

os.system("clear")

pwd = input('STEP 1: Plase Enter "pwd" : ')
while pwd.strip() != "pwd":
    pwd = input('STEP 1: Plase Enter "pwd" : ')

def pwds():
    if pwd == "pwd":
        os.system("pwd")
        print("###", pwd, "is command for show work on directoris")
pwds()

print("*" * 50)

ls = input('STEP 2: Plase Enter "ls" : ')
while ls.strip() != "ls":
    ls = input('STEP 2: Plase Enter "ls" : ')
if ls == "ls":
    os.system("ls")
    print("###", ls, "is command for show directoris and file in current dir")

print("*" * 50)

ls_l = input('STEP 2.1 : Plase Enter "ls -l " : ')
while ls_l.strip() != "ls -l":
    ls_l = input('STEP 2.1 : Plase Enter "ls -l" : ')
if ls_l == "ls -l":
    os.system("ls -l")
    print("###", ls_l, "is command for show directoris and file in current dir  ")

print("*" * 50)

who_am_i = input('STEP 3 : Plase Enter "whoami " : ')
while who_am_i.strip() != "whoami":
    who_am_i = input('STEP 3 : Plase Enter "whoami" : ')
if who_am_i == "whoami":
    os.system("whoami")
    print("###", who_am_i, "is command for show user login in system  ")

print("*" * 50)

uname_a = input('STEP 4 : Plase Enter "uname -a" : ')
while uname_a.strip() != "uname -a":
    uname_a = input('STEP 4 : Plase Enter "uname -a" : ')
if uname_a == "uname -a":
    os.system("uname -a")
    print("###", uname_a, "is command for show kernel version ")

print("*" * 50)

w = input('STEP 5 : Plase Enter "w" : ')
while w.strip() != "w":
    w = input('STEP 5 : Plase Enter "w" : ')
if w == "w":
    os.system("w")
    print("###", w, "is command for Show who is logged on and what they are doing ")

print("*" * 50)

mkdir= input('STEP 6 : Plase Enter "mkdir ((enter a name like test))" : ')
while mkdir.strip() != "mkdir test":
    mkdir = input('STEP 6 : Plase Enter "mkdir" : ')
if mkdir == "mkdir test":
    os.mkdir("test")
    print("###", mkdir, "is command for create directori ")

print("*" * 50)

dir = ("/home/majid/Documents/myproject/test")
cd= input('STEP 7 : Plase Enter "cd ((enter a name crate directoris like test))" : ')
while cd.strip() != "cd test":
    cd = input('STEP 7 : Plase Enter "cd" : ')
if cd == "cd test":
    os.chdir(dir)
    print("###", cd, "is command for change directori ")
# print ("### now your current directoris is: ", os.getcwd())
pwds()
print("*" * 50)
