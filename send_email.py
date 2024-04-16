import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body):
    host = "smtp.gmail.com"
    port = 465
    username = "dashmeetsingharora@gmail.com"
    password = "rajdyiuopqgupnsw"  # Be sure to manage passwords securely
    receiver = "dashmeetsingharora@gmail.com"

    # Set up the MIME message
    message = MIMEMultipart()
    message['From'] = username
    message['To'] = receiver
    message['Subject'] = subject

    # Attach the body text
    message.attach(MIMEText(body, 'plain', 'utf-8'))

    context = ssl.create_default_context()

    # Send the email
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.send_message(message)  # This uses the new API for MIME messages

    print("Email sent successfully!")
