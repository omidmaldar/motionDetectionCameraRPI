import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
# print the ip address on screen
print(s.getsockname()[0])
# save it for our later use
imAt = s.getsockname()[0]
s.close()

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "EMAIL-Address"
toaddr = "EMAIL-Address"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "IP Address"
msg.attach(MIMEText(imAt, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "EMAIL-SMTP-PASSWORD-COMES-HERE")

text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)

server.quit()

