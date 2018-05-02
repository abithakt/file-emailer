import ruamel.yaml as yaml
import smtplib
import gnupg
from sys import argv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

with open("config.yml", 'r') as ymlfile:
    config = yaml.safe_load(ymlfile)

sender = smtplib.SMTP_SSL(config['smtp_server'], config['smtp_port'])
sender.login(config['sender'], config['password'])

gpg = gnupg.GPG(
    binary=config['gnupg'],
    homedir=config['gpg-home'],
    keyring=config['keyring'],
    secring=config['secring'])

encryptedemail = MIMEMultipart('alternative')
encryptedemail['Subject'] = argv[1]
encryptedemail['From'] = config['sender']
encryptedemail['To'] = config['recipient']

with open(argv[1]) as thefile:
    email_text = MIMEText(str(gpg.encrypt(
        thefile.read(), # message content
        config['recipient-key'],
        default_key=config['sender-key'],
        passphrase=config['passphrase'],
        armor=True,
        encrypt=True,
    )), 'plain')
    encryptedemail.attach(email_text)

sender.send_message(encryptedemail)

sender.quit()
