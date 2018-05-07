# file-emailer: Email a file to yourself
# Author: Abitha K Thyagarajan <abitha@pm.me>
# Copyright (C) 2018 Abitha K Thyagarajan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


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
        encrypt=True,
    )), 'plain')
    encryptedemail.attach(email_text)

sender.send_message(encryptedemail)

sender.quit()
