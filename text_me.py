import smtplib, email, getpass
from email.MIMEText import MIMEText

smtp_host = "smtp.gmail.com"
smtp_port = 587
server = smtplib.SMTP()
server.connect(smtp_host, smtp_port)

server.set_debuglevel(1)

server.starttls()
server.login(raw_input("What is your Gmail email address: "),
				getpass.getpass())

server.sendmail("From (seems useless...)",
				 raw_input("Enter a Sprint cell number: ")+ "@pm.sprint.com",
				 raw_input("Enter a msg: "))

