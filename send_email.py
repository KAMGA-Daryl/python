#import section
 import smtplib
 import json
 from email.message import EmailMessage


 #load config (gmail) from json file
 json_file = open("config.json")
 gmail_cfg = json.load(json_file)

 print(gmail_cfg)

 #Create the message to send
 msg = EmailMessage()
 msg["to"] = gmail_cfg["email"]
 msg["from"] = gmail_cfg["email"]
 msg["subject"] = "Send email with python"
 msg.set_content("Hil this xas sent from python script !")


 #Create smtp, login to gmail and send the email
with smtplib.SMTP_SSL(gmail_cfg["server"],gmail_cfg["port"]) as smtp:
  smtp.login(gmail_cfg["email"],gmail_cfg[ "pwd"])
  smtp.send_message(msg)
  print("Email sent  ! ")



