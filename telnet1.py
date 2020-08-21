# https://docs.python.org/3.1/library/telnetlib.html

import getpass
import telnetlib

HOST = "192.168.122.71"  #we are connecting to this IP
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST) #Telnet lib is now leveraged to telnet to the host

tn.read_until(b"Username: ") #this is what is prompted when you telnet to a cisco router
tn.write(user.encode('ascii') + b"\n") #script sends the entered username to the router
if password:   #if a password is configured for the telnet session
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n") #password sent to the router for authN

tn.write(b"enable\n") #takes us to enable mode of the router
tn.write(b"cisco\n") #enter password to take us to privilege mode.
tn.write(b"conf t\n")
tn.write(b"int loop 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255 \n")
#Enabling OSPF
tn.write(b"router ospf 1\n")
tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")

tn.write(b"end\n") #takes us back to privilege mode
tn.write(b"exit\n") #exit the telnet session

print(tn.read_all().decode('ascii'))