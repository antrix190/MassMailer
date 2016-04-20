import csv 
import smtplib
from email.mime.text import MIMEText
import re
from mail import *
from contants import *

def massmail():
    with open('/path/to/csv/file', 'r') as file:
        data=file.read()
        data = re.split("[,\n]+", data)
        if len(data[-1]) <1:
            data = data[:-1]
    
    f = open( "/path/to/html/content/file", "r" )
    body = f.read()
    f.close()
    
    return body, data

if __name__ == '__main__':
    body, send_to = massmail()
    attachment =[]    #['server path of the file1','server path of the file2']
    
    for each in send_to:
        #Adding Tracking HTML element
        if mailType == 'html':
            src = "http://scraper.exclusively.net/api/report/"+each+"?subject="+subject
            temp_body = ""
            temp_body = "<img src=\""+src+"\" style='visibility: hidden;' />"+ body

        list_send_to =  []
        list_send_to.append(each)
        send_mail(send_from,list_send_to,subject,temp_body,attachment,"smtp.gmail.com",587,username,password,'True', mailType)
