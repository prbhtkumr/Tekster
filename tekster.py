#!/usr/bin/env python
import os
import random
import base64
def clr():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

clr()
print("This Tool Is Used To Send Anonyous Messages\n\n")
print("Make sure you have proxychains setup.\n\n")
print("Enter The Details Of The Person You Want To Send Anonymous Message")
cc = input("\tEnter Country Code (Without +) : ")
if '+' in cc:
        tc = list(cc)
        tc.remove('+')
        cc = ''.join(tc)
        cc = cc.strip()
if len(cc) 