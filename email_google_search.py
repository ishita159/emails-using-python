# Python code to illustrate Sending mail with attachments
# from your Gmail account

# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import urllib2
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search

query = raw_input("Enter search query: ")
sub_str = "python-tutorial"
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    if (j.find(sub_str) != -1):
       # print(j)
        response = urllib2.urlopen(j)
        with open('output1.txt', 'w') as f:
           f.write(response.read())


fromaddr = "singhishita159@gmail.com"
toaddr = "shantanushukla61@gmail.com"


# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = fromaddr

# storing the receivers email address
msg['To'] = toaddr

# storing the subject
msg['Subject'] = "Subject of the Mail"

# string to store the body of the mail
body = "Baby Yoda has sent you something"

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
filename = "output.txt"
attachment = open("/home/ishita/Documents/MyPrograms/emails_using_python/output.txt", "rb")

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload((attachment).read())

# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(p)

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(fromaddr, "Ishita@009")

# Converts the Multipart msg into a string
text = msg.as_string()

# sending the mail
s.sendmail(fromaddr, toaddr, text)

# terminating the session
s.quit()
