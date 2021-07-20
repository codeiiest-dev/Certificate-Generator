

# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import smtplib
from string import Template
import os


def send_mail(s: smtplib.SMTP, message_template: Template, name: str,
              dest_email: str, src_email: str, mail_subject:str, image_file: str,
              cc: str, bcc:str):
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    message = message_template.substitute(PERSON_NAME=name.title())

    # setup the parameters of the message
    msg['From'] = src_email
    msg['To'] = dest_email
    msg['Subject'] = mail_subject
    msg['Cc'] = cc
    msg['Bcc'] = bcc

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    #read and attach image to mail
    with open(image_file, 'rb') as f:
        img_data = f.read()

    image = MIMEImage(img_data, name=os.path.basename(image_file))
    msg.attach(image)

    # send the message via the server set up 
    s.send_message(msg)
