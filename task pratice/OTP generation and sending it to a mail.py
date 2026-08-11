#OTP generation and sending it to the mail

import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email details
From = "proshankumar8555@gmail.com"
To = "venkysangiseety621@gmail.com"

# Generate 6-digit OTP
otp = random.randint(100000, 999999)

print("Generated OTP:", otp)

# Subject
Subject = "OTP Verification"

# Email body
body = f"""
Hello,

Your OTP is: {otp}

Please do not share this OTP with anyone.

Thank you.
"""

# Create email
msg = MIMEMultipart()

msg["From"] = From
msg["To"] = To
msg["Subject"] = Subject

# Add body
msg.attach(MIMEText(body, "plain"))

# Connect to Gmail SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)

# Start secure connection
server.starttls()

# Login using Gmail App Password
server.login(From, "rsac jlxf vhby divm")

# Send email
server.sendmail(From, To, msg.as_string())

print("OTP sent successfully!")

# Close server
server.quit()
