import os
import pyotp
import time
import qrcode
import getpass

#collect pass
passw=open("pass.txt",mode="r")
twoqs=open("question.txt",mode="r")
pass_lst=[]
for line in passw:
    password=line.split()
    for t in password:
        pass_lst.append(t)
pass_qs=twoqs.read()
passw.close()
twoqs.close()

#checking pass verification
os.system("echo MFA authentication | pv -qL 20")
os.system("echo ░▒█▀▄▀█░▒█▀▀▀░█▀▀▄░█░▒█░▀█▀░█░░░░█▀▀░█▀▀▄░▀█▀░░▀░░█▀▄░█▀▀▄░▀█▀░▄▀▀▄░█▀▀▄ | pv -qL 100")
os.system("echo ░▒█▒█▒█░▒█▀▀░▒█▄▄█░█░▒█░░█░░█▀▀█░█▀▀░█░▒█░░█░░░█▀░█░░░█▄▄█░░█░░█░░█░█▄▄▀ | pv -qL 100")
os.system("echo ░▒█░░▒█░▒█░░░▒█░▒█░░▀▀▀░░▀░░▀░░▀░▀▀▀░▀░░▀░░▀░░▀▀▀░▀▀▀░▀░░▀░░▀░░░▀▀░░▀░▀▀ |pv -qL 100")
os.system("echo Enter passcode| pv -qL 20")
ch_pass=getpass.getpass()
if ch_pass == pass_lst[0]:
    print ("Level 1 PASS")
else:
    print("Wrong password FAILED")
    exit(0)

print(pass_qs + " ?")
qs_ans=input()
if qs_ans == pass_lst[1]:
    print ("Level 2 PASS")
else:
    print("Wrong password FAILED")
    exit(0)


os.system("echo Enter OTP from authenticator app| pv -qL 15")
totp = pyotp.TOTP('base3222secret3232')
b=totp.now()

a=totp.verify(input("Enter authentication code: "))

if a == True:
    print("MultiFactorAuthentication approved")
    pp=1
else:
    b=str(a)
    print(b + " is wat you are")
    print("MultiFactorAuthentication failed")


if pp == 1:
    os.system("nano ~/Downloads/MFA/enc/enc.txt")