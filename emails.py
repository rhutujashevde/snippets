import imaplib
import base64
import os
import email


mail = imaplib.IMAP4_SSL("imap.gmail.com",993)

mail.login('email','pass')

mail.select('Inbox')

type, data = mail.search(None, '(SUBJECT "OTRC")')

for num in reversed(data[0].split()):
    typ, data1 = mail.fetch(num, '(RFC822)' )
    raw_email = data1[0][1]
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)
    sub = email_message['subject']
    print sub
    if "OTRC" in sub:
        lis.append(sub)
