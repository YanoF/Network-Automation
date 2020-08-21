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
tn.write(b"vlan 2\n") #create a VLAN
tn.write(b"name Python_VLAN 2 \n")
tn.write(b"vlan 3\n") #create a VLAN
tn.write(b"name Python_VLAN 3 \n")
tn.write(b"vlan 4\n") #create a VLAN
tn.write(b"name Python_VLAN 4 \n")
tn.write(b"vlan 5\n") #create a VLAN
tn.write(b"name Python_VLAN 5 \n")
tn.write(b"vlan 6\n") #create a VLAN
tn.write(b"name Python_VLAN 6 \n")
tn.write(b"end\n") #takes us back to privilege mode
tn.write(b"exit\n") #exit the telnet session

print(tn.read_all().decode('ascii'))