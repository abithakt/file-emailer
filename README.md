file-emailer
============


[![Made with Python3](https://img.shields.io/badge/Made%20with-Python3-1f425f.svg)](https://www.python.org/)
[![License: GPLv3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/abithakt/file-emailer/blob/master/LICENSE)


This is a small program that sends a file as the body of an encrypted email.



## Table of contents

  - [Getting started](#getting-started)
  - [Usage](#usage)
  - [Planned features](#planned-features)
  - [Contributing](#contributing)
  - [License](#license)



## Getting started

1. Download and install [Python3](https://www.python.org/).

2. Clone or [download](https://github.com/abithakt/file-emailer/archive/master.zip) this repository.

2. Navigate to the folder and install the dependencies:
    ```
    pip3 install -r requirements.txt
    ```
    or
    ```
    py -m pip install -r requirements.txt
    ```

3. Rename `example-config.yml` to `config.yml`. Edit it to include your details:

    1. Put your email address and password under `sender` and `password`. This is the address from which emails will be sent.
    2. Under `sender-key` and `passphrase`, put your public key fingerprint and its passphrase.
        * You can determine the fingerprint of a key by running `$ gpg --fingerprint`, which lists all keys with their fingerprints, or `$ gpg --fingerprint [email address]` to view the fingerprint of the key associated with an email address.
    3. Put the recipient's email address and their public key fingerprint under `recipient` and `recipient-key`.
    4. Under `gnupg`, put the path to your gpg binary. You can determine this by running `$ which gpg`.
    5. Under `gpg-home`, `keyring`, and `secring`, enter your gpg home directory, public keyring, and secret keyring.
        * Run `$ gpg --list-keys`. The output will be something like `/path/to/pubring.gpg`. In this example, `pubring.gpg` is your public keyring, and the rest of the path is your gpg home directory.
        * Similarly, to find the name of your secret keyring, run `$ gpg --list-secret-keys`. The output will be of the form `/path/to/secring.gpg`. Here, `secring.gpg` is the name of your secret keyring.
    6. Under `smtp_server` and `smtp_port`, put your email provider's SMTP server and port.

6. Run `file-emailer.py`.
    ```
    python3 file-emailer.py /path/to/file
    ```
    or
    ```
    py file-emailer.py /path/to/file
    ```



## Usage

Run

```
python3 file-emailer.py /path/to/file
```

or

```
py file-emailer.py /path/to/file
```

where `file` is the one you want to send.



## Planned features

  - [x] ~~Change email subject to filename~~
  - [ ] Make subject optional
  - [ ] Add support for multiple files
  - [ ] Add support for multiple recipients
    - [ ] Make recipient(s) a command-line argument?
  - [ ] Create version without PGP



## Contributing

  * Please submit issues and feature requests [here](https://github.com/abithakt/file-emailer/issues).
  * Pull requests are welcome.
  * For queries and more information, feel free to email me.



## License

**file-emailer** is licensed under the GPLv3. For more details, see [LICENSE](LICENSE).

Copyright (C) 2018 Abitha K Thyagarajan

> This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

> This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

> You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
