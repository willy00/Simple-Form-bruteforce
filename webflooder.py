import sys
import datetime
import selenium
import requests
import random
import string
from pathlib import Path
import time as t
from sys import stdout
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import init as colorinit
from colorama import Fore, Style
#colorama init
colorinit(autoreset=True)
#func to setup the program
def wizard():
    print(banner)
    webinput = input(Fore.GREEN + Style.BRIGHT + "\n[~] " + Fore.WHITE + "Enter a website: " + Style.RESET_ALL) #input domain name
    website = "http://" + webinput #auto add the http in front
    sys.stdout.write(Style.BRIGHT + Fore.GREEN + "[!] "+Fore.WHITE + "Checking if site exists "),
    sys.stdout.flush()
    t.sleep(1)
    #check if site input is valid by using requests. 
    try:
        request = requests.get(website)
        if request.status_code == 200: #get HTTP status code 200 = site input is valid
            print (Style.BRIGHT + Fore.GREEN + "[OK]"+Fore.WHITE)
            sys.stdout.flush()
    except selenium.common.exceptions.NoSuchElementException:
        pass
    except:
        #if website not found AKA status code != 200
        t.sleep(1)
        print (Style.BRIGHT + Fore.RED + "[X]"+Fore.WHITE)
        t.sleep(1)
        print (Style.BRIGHT + Fore.RED + "[!]"+Fore.WHITE+ " Server IP address cannot be found")
        exit()
    username_selector = input(Style.BRIGHT + Fore.GREEN + "[~] " + Fore.WHITE + "Enter the username selector: " + Style.RESET_ALL) #input CSS selector
    password_selector = input(Style.BRIGHT + Fore.GREEN + "[~] " + Fore.WHITE + "Enter the password selector: " + Style.RESET_ALL) #input CSS selector
    login_btn_selector = input(Style.BRIGHT + Fore.GREEN + "[~] " + Fore.WHITE + "Enter the Login button selector: " + Style.RESET_ALL) #input CSS selector
    name_list = input(Style.BRIGHT + Fore.GREEN + "[~] " + Fore.WHITE + "Enter location to name list: " + Style.RESET_ALL) #location of name list
    try:
        Path(name_list).resolve(strict=True)
    except FileNotFoundError:
        print(Style.BRIGHT + Fore.RED + "[!]" + Fore.WHITE + " File not found, make sure that the path to the file is correct")
        exit()
    else:
        pass
    pass_list = input(Style.BRIGHT + Fore.GREEN + "[~] " + Fore.WHITE + "Enter location to a password list: " + Style.RESET_ALL) #location of password list
    try:
        Path(pass_list).resolve(strict=True)
    except FileNotFoundError:
        print(Style.BRIGHT + Fore.RED + "[!]" + Fore.WHITE + " File not found, make sure that the path to the file is correct")
        exit()
    else:
        pass
    is_iframe = input(Style.BRIGHT + Fore.GREEN + "[~] " + Fore.WHITE + "Is element in iframe?(Y/N) " + Style.RESET_ALL) #input if form is in iframe
    if is_iframe == "y" or is_iframe == "Y":
        iframe_sel = input(Style.BRIGHT + Fore.GREEN + "[~] " + Fore.WHITE + "Enter the iframe selector: " + Style.RESET_ALL) #input iframe CSS selector
    else:
        pass
    other_var_1 = input(Style.BRIGHT + Fore.GREEN + "[~] " + Fore.WHITE + "Any addtional input selector?(Y/N) " + Style.RESET_ALL) #prompt user for more selector if any
    if other_var_1 == "Y" or other_var_1 == "y":
        other_1_type = input(Style.BRIGHT + Fore.GREEN + "[~] " + Fore.WHITE + "Input type?(radio/email/password/checkbox) " + Style.RESET_ALL) #check input type
        other_1_sel = input(Style.BRIGHT + Fore.GREEN + "[~] " + Fore.WHITE + "Enter the selector: " + Style.RESET_ALL) #input CSS selector
        other_var_2 = input(Style.BRIGHT + Fore.GREEN + "[~] " + Fore.WHITE + "Any addtional input selector?(Y/N) " + Style.RESET_ALL) # prompt for more selector Max 2 addtional inputs
        if other_var_2 == "Y" or other_var_2 == "y":
            other_2_type = input(Style.BRIGHT + Fore.GREEN + "[~] " + Fore.WHITE + "Input type?(radio/email/password/checkbox) " + Style.RESET_ALL) #check input type
            other_2_sel = input(Style.BRIGHT + Fore.GREEN + "[~] " + Fore.WHITE + "Enter the selector: " + Style.RESET_ALL) #input CSS selector
        #setting var to NULL if not used, else python will complain(or not idk)
        else:
            other_2_sel = None 
            other_2_type = None
            pass
    else:
        other_1_sel = None
        other_1_type = None
        other_2_sel = None
        other_2_type = None
        pass
    flood(iframe_sel, name_list, username_selector ,password_selector,login_btn_selector,pass_list, website, is_iframe, other_1_sel, other_1_type, other_2_sel, other_2_type)
#function to generate random 3 digit numbers
def randomDigits(stringLength=3):
    Digits = string.digits
    return ''.join(random.choice(Digits) for i in range(stringLength))
#spam function
def flood(iframe_sel, name_list, username_selector ,password_selector,login_btn_selector,pass_list, website, is_iframe, other_1_sel, other_1_type, other_2_sel, other_2_type):
    r = open(name_list, 'r') #read name list
    f = open(pass_list, 'r') #read pass list
    #driver = webdriver.Chrome()
    optionss = webdriver.ChromeOptions() #setting driver options
    optionss.add_argument("--disable-popup-blocking") 
    optionss.add_argument("--disable-extensions")
    browser = webdriver.Chrome(options=optionss)
    while True:
        try:
            for line in r: #for every line in name list file do these stuff
                name_extra = ''.join(randomDigits())
                username = line.lower() + name_extra #generate a username base on name list
                email = username + "@gmail.com" #add "@gmail.com" behind the username to make it look like a email
                for line in f: #for every line in password list file do these stuff
                    password = line #set password var to a line from pass list
                    break
                browser.get(website)
                t.sleep(3)
                if is_iframe == "Y" or is_iframe == "y": #if element in iframe switch focus to frame
                    browser.switch_to.frame(browser.find_element_by_css_selector(iframe_sel))
                if other_1_type != None: #if var not NULL
                    if other_1_type == "checkbox" or other_1_type == "radio": #check input type, if radio/checkbox
                        browser.find_element_by_css_selector(other_1_sel).click() #click on checkbox/radio
                    elif other_1_type == "password": #if input type = password
                        browser.find_element_by_css_selector(other_1_sel).send_keys(password) #input password
                    else:
                        browser.find_element_by_css_selector(other_1_sel).send_keys(email) #else input email
                        pass
                else:
                    pass
                #same as ^^
                if other_2_type != None:
                    if other_2_type == "checkbox" or other_2_type == "radio":
                        browser.find_element_by_css_selector(other_2_sel).click()
                    elif other_2_type == "password":
                        browser.find_element_by_css_selector(other_2_sel).send_keys(password)
                    else:
                        browser.find_element_by_css_selector(other_2_sel).send_keys(email)
                        pass
                else:
                    pass
                Sel_user = browser.find_element_by_css_selector(username_selector) #Finds Selector
                Sel_pas = browser.find_element_by_css_selector(password_selector) #Finds Selector
                Sel_user.send_keys(username) #submit the data
                Sel_pas.send_keys(password) #submit the data
        except KeyboardInterrupt: #exit program ctrl C is used
            exit()
        except selenium.common.exceptions.NoSuchElementException:
            print("AN ELEMENT HAS BEEN REMOVED FROM THE PAGE SOURCE OR WAS NOT FOUND.")
            exit()
banner = Style.BRIGHT + Fore.RED +'''
  

 __          __  _        __ _                 _           
 \ \        / / | |      / _| |               | |          
  \ \  /\  / /__| |__   | |_| | ___   ___   __| | ___ _ __ 
   \ \/  \/ / _ \ '_ \  |  _| |/ _ \ / _ \ / _` |/ _ \ '__|
    \  /\  /  __/ |_) | | | | | (_) | (_) | (_| |  __/ |   
     \/  \/ \___|_.__/  |_| |_|\___/ \___/ \__,_|\___|_|   
                                                           
                                                           


  {0}[{1}-{2}]--> {3}V.1.0
  {4}[{5}-{6}]--> {7}coded by a_idiot
  {8}[{9}-{10}]-->{11} A tool to troll scammers                      '''.format(Fore.RED, Fore.WHITE,Fore.RED,Fore.GREEN,Fore.RED, Fore.WHITE,Fore.RED,Fore.GREEN,Fore.RED, Fore.WHITE,Fore.RED,Fore.GREEN)

wizard()