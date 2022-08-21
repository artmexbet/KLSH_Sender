import smtplib

from cfg import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

message = MIMEMultipart("alternative")
message["Subject"] = "Тест"
message["From"] = LOGIN
message["To"] = "2004maydurov@mail.ru"

part = MIMEText(open("test.html", encoding="utf-8").read(), "html")
message.attach(MIMEText("Привет", "plain"))
message.attach(part)

smtp = smtplib.SMTP("smtp.gmail.com", 587)
smtp.starttls()
smtp.login(LOGIN, PASSWORD)
smtp.sendmail(LOGIN, "maydurov2004@yandex.ru", message.as_string())
