import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "singhishita159@gmail.com"
you = "shantanushukla61@gmail.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\n https://www.epicreads.com/blog/16-extremely-romantic-quotes-you-should-say-to-your-love/sss"
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       You need to love me more get it?<br>
       Here is the <a href="https://www.epicreads.com/blog/16-extremely-romantic-quotes-you-should-say-to-your-love/">FROM LOVE</a> that you need to see today <3.
    </p>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)
# Send the message via local SMTP server.
mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('singhishita159@gmail.com', 'Ishita@009')
mail.sendmail(me, you, msg.as_string())
mail.quit()
