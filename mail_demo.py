# Python code to illustrate Sending mail from
# your Gmail account
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("singhishita159@gmail.com", "Ishita@009")

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail("singhishita159@gmail.com", "singhishita1599@gmail.com", message)

# terminating the session
s.quit()
