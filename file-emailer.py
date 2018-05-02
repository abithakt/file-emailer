import ruamel.yaml as yaml
import smtplib
import gnupg
#import mimetypes
from sys import argv
from subprocess import run

#from email.message import Message
#from email.header import Header
#from email.encoders import encode_base64
#from email.utils import formatdate, make_msgid
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

#f = argv[1]
#thefile = open(f)
#pasph = input('passphrase: ')

encryptedemail = MIMEMultipart('alternative')
encryptedemail['Subject'] = "test"
encryptedemail['From'] = config['sender']
encryptedemail['To'] = config['recipient']
#email_text = MIMEText(gpg.encrypt(thefile.read().encode('ascii'), config['recipient'], config['sender-key'], pasph))
#email_text = MIMEText(gpg.encrypt(str(thefile.read()).encode('ascii'), config['sender']))

"""def encrypt(filename):
    result = run("gpg -es " + filename, stdout=subprocess.PIPE, input=config['passphrase'])
    return result.stdout.decode('utf-8')"""


with open(argv[1]) as thefile:
    #email_text = MIMEText(thefile.read()
    #sender.sendmail(email_text, config['sender'], config['sender'])
    email_text = MIMEText(str(gpg.encrypt(
        thefile.read(),
        config['recipient-key'],
        default_key=config['sender-key'],
        passphrase=config['passphrase'],
        armor=True,
        encrypt=True,
    )), 'plain')
    encryptedemail.attach(email_text)

    sender.send_message(encryptedemail)

sender.quit()
