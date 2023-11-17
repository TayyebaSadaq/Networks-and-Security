import smtplib # protocol to s end emails
from email import encoders # to encode the email
from email.mime.text import MIMEtext # ordinary text
from email.mime.base import MIMEbase # attach files
from email.mime.multipart import MIMEMultipart # to send both text and files

server = smtplib.SMTP('smtp.gmail.com', 25) # server and port

server.ehlo() # identify ourselves with the mail server

server.login('mail@mail.com', 'password') # login to the mail server

msg = MIMEMultipart() # create a message
msg['From'] = 'Sender Name'
msg['To'] = 'Receiver Name'
msg['Subject'] = 'Just a test'

# with open('message.txt', 'r') as f:
#     message = f.read()
# msg.attach() # attach the file