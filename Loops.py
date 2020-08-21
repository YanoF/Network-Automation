#Our VLAN script is not so effecctive if we have to create like 100 VLANS.
#We shall improve on it by using loops

import getpass
import telnetlib

HOST = "192.168.122.72"  #we are connecting to this IP
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

for n in range (2,12): #range of VLANS to be created
    tn.write(b"vlan " + str(n).encode('ascii')+ b"\n") #create a VLAN, change VLAN number to string then encode as ascii text
    tn.write(b"name Python_VLAN " + str(n).encode('ascii')+ b"\n")

tn.write(b"end\n") #takes us back to privilege mode
tn.write(b"wr\n") #save the configs
tn.write(b"exit\n") #exit the telnet session

print(tn.read_all().decode('ascii'))