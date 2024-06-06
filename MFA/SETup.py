import os
import sys
import getpass 
import pyotp
import qrcode

def setup ():
    os.system("echo Encrytion Software | pv -qL 10")
    #Run once
    passw = getpass.getpass("Enter password:")
    os.system("echo Setting up MFA| pv -qL 20")
    fp=open("pass.txt",mode="w")
    qs=open("question.txt",mode="w")
    os.system("echo Setting up 2factor | pv -qL 10")
    twof=input("Enter A security question:\n")
    os.system("clear")
    twof_ans=input(twof + "?\n")
    fp.write(passw + " " + twof_ans)
    fp.close()
    qs.write(twof)
    qs.close()
    os.system("echo Enter filepath of the file to be secured| pv -qL 20")
    filepath=input()
    fp=open("filep.txt",mode="w")
    fp.write(filepath)
    fp.close()
    os.system("sudo mv " + filepath + " ~/Downloads/MFA/enc" )
setup()

