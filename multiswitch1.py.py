
import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your remote account: ")
password = getpass.getpass()

f = open ('myswitches') #myswitches file is stored in the netwok automation container.

for IP in f:
    IP=IP.strip() #strips trailing spaces
    print ("Configuring Switch " + (IP))
    HOST = IP #read from the myswitches file.
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
       tn.read_until(b"Password: ")
       tn.write(password.encode('ascii') + b"\n")
    #tn.write(b"enable\n") #from previous labs, this is already enabled on the switches   
    tn.write(b"conf t\n")
    tn.write(b"vlan 2\n")
    tn.write(b"name Python_VLAN_2\n")
    tn.write(b"exit\n")
    tn.write(b"vlan 3\n")
    tn.write(b"name Python_VLAN_3\n")
    tn.write(b"exit\n")
    tn.write(b"vlan 4\n")
    tn.write(b"name Python_VLAN_4\n")
    tn.write(b"exit\n")
    tn.write(b"vlan 5\n")
    tn.write(b"name Python_VLAN_5\n")
    tn.write(b"exit\n")
    tn.write(b"vlan 6\n")
    tn.write(b"name Python_VLAN_6\n")
    tn.write(b"vlan 7\n")
    tn.write(b"name Python_VLAN_7\n")
    tn.write(b"vlan 8\n")
    tn.write(b"name Python_VLAN_8\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))