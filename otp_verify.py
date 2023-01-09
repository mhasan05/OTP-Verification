# OTP Verification using Python
# https://teamerror.net/


import math
import random
import smtplib,ssl
port = 465
smtp_server ="smtp@example.com" #Enter your SMTP server
user = "example@example.com" #Enter Host Email Address
password = "emailpass" #Enter Host email Password
sender = "example@example.com" #Enter Host Email Address
receivers = ['receiver@example.com'] #Enter Receiver Email Address
def VerifyOTP():
    code ="0123456789"
    OTP = ""
    for i in range(6):
        OTP+=code[math.floor(random.random()*10)]
    otp = OTP + " is your verification code"
    mgs = otp
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL(smtp_server,port,context)
    server.login(sender,password)
    email = input("Enter your email address:")
    server.sendmail(sender, email,mgs)
    a = input("Enter your OTP:")
    if a == OTP:
        return True
    else:
        return False

a = VerifyOTP()
print(a)
