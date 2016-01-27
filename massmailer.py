import csv 
import smtplib
from email.mime.text import MIMEText
import re
from includes.mail import *

def massmail():
    with open('/home/antariksh/Desktop/message.csv', 'r') as file:
        data=file.read()
        data = re.split("[,\n]+", data)
        if len(data[-1]) <1:
            data = data[:-1]
    
    f = open( "/home/antariksh/Desktop/message.csv", "r" )
    body = []
    for line in f:
        body.append(line)
    f.close()
    body = ''.join(body)
    
    return body, data

if __name__ == '__main__':
    body, send_to = massmail()
    attachment =[] #['server path of the file1','server path of the file2']
    send_mail(send_from,send_to,'test',body,attachment,"smtp.gmail.com",587,username,password,'True')
