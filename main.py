import smtplib
from email.mime.text import MIMEText
# Body of E-mail
msg = MIMEText("This is Body of Email............")
# Subject of E-mail
msg['Subject'] = "This is Subject of Email........."
# Sender E-mail Id
sender = 'abc@company.com'
msg['From'] = sender
# Receiver E-mail Id
recipient = 'abc@gmail.com'
msg['To'] = recipient
# SMTP Server
server = smtplib.SMTP_SSL('smtppro.zoho.in', 465)
# SMTP Server Login Credentials
server.login(sender, 'password123')
# Gives Send Mail Request to SMTP Server
server.sendmail(sender, recipient, msg.as_string())
# Quit or Logout from SMTP Server 
server.quit()