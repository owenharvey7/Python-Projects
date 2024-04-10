# Importing the necessary libraries
import smtplib
import ssl
from email.message import EmailMessage

# Defining the sender's email address and password
sender_email = 'youremail@gmail.com'
password = open("password.txt", "r").read()

# Defining the receiver's email address
receiver_email = input("Enter the receiver's email address: ")

# Defining the subject of the email
subject = input("Enter the subject of the email: ")

# Defining the body of the email
body = input("Enter the body of the email: ")

# Creating the email message
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
    <html>
        <body>
            <h1>{subject}</h1>
            <p>{body}</p>
        </body>
    </html>
"""

message.set_content(html, subtype="html")

context = ssl.create_default_context()

print("Sending the email...")

# Sending the email

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email sent successfully!")


