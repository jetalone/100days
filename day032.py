import smtplib

my_email = "anobscurereference@gmail.com"
password = "5money$%^"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="willxmelton@gmail.com", msg="Hello")
connection.close()