import smtplib, email, getpass
from email.MIMEText import MIMEText

smtp_host = "smtp.gmail.com"
smtp_port = 587
server    = smtplib.SMTP()
server.connect(smtp_host, smtp_port)

#server = smtplib.SMTP("smtp.gmail.com", 587)
server.set_debuglevel(1)

server.ehlo()
server.starttls()
server.login(raw_input("What is your email address: "),
				 getpass.getpass())
fromaddr = raw_input("Send mail by the name of: ")
tolist = raw_input("To: ").split()
sub = raw_input("Subject: ")

msg = email.MIMEMultipart.MIMEMultipart()
msg["From"] = fromaddr
msg["To"] = email.Utils.COMMASPACE.join(tolist)
msg["Subject"] = sub
msg.attach(MIMEText(raw_input("Body: ")))
msg.attach(MIMEText("\nsent via python", "plain"))
server.sendmail("crazcalm@gmail.com", tolist, msg.as_string())

