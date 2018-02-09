#!/usr/bin/env python3
# coding: utf-8

from email.mime.text import MIMEText
import smtplib
from email.header import Header

msg = MIMEText('Hello, Byng send for Python...', 'plain', 'utf-8')
msg['From'] = Header("Byng", 'utf-8')
msg['To'] = Header("Byng", 'utf-8')
msg['Subject'] = Header("Send from Python", 'utf-8')

from_addr = input('From:')
password = input('password:')
to_addr = input('To:')
smtp_server = input('SMTP Server:')
port = input('Port:')


#server = smtplib.SMTP(smtp_server, port)
server = smtplib.SMTP()
server.connect(smtp_server, port)
server.set_debuglevel(1)
#server.ehlo()
#server.starttls()
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()

