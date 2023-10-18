import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration

sender_email = 'your_email@gmail.com'
receiver_email = 'recipient_email@example.com'
subject = 'Subject of the Email'
message = 'This is the body of the email.'

# Create an instance of MIMEMultipart
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the message to the email
msg.attach(MIMEText(message, 'plain'))

# SMTP server configuration for Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'your_email@gmail.com'
smtp_password = 'your_password'

# Establish an SMTP connection
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # Enable TLS encryption
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())

print('Email sent successfully!')
