# Web Form Flooder
![Latest version](https://img.shields.io/badge/-v1.0-brightgreen.svg)

This is a program that uses the selenium webdriver to automatically fill in forms. It identifies the input fields using the CSS selector provided by the user and will automatically fill in data based on the input type. Username are generated from a name list provided by the user.
Supported input types:
* radio
* checkbox
* email
* password
* username

#Installation

##Requirements

* requests
* selenium
* colorama

## Running this on Debian based systems

...

sudo apt-get install python3-pip python3 git
git clone https://github.com/willy00/Web-Flooder
cd Web-Flooder
python3 -m pip install -r requirements.txt
python3 webflooder.py
...

## Running this on a Windows system
Download the zip folder and extract it
Open comand prompt in the folder
...

(path to python3) -m pip install -r requirements.txt
(path to python3) webflooder.py
...