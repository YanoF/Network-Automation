#this scripts backs up the running configs to the network automation container.

import getpass
import telnetlib

user = input('Enter your telnet username: ')
password = getpass.getpass()

f = open('myswitches')

for IP in f:
    IP=IP.strip()
    print ('Get running config from Switch ' + (IP)) #script is getting the running configs from the switch with the said IP
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')
    if password:
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b'\n')  
    tn.write(b"terminal length 0\n") #shows the entire output page, rather than the default 24 lines.
    tn.write(b"show run\n")
    tn.write(b'exit\n')

    readoutput = tn.read_all()
    saveoutput =  open("switch" + HOST, "w") #saving the running configs
    saveoutput.write(readoutput.decode('ascii'))
    saveoutput.write("\n")
    saveoutput.close
