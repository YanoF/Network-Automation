#from security stand point, it is not a best practice to hard code credentials into a script.
#this scripts shows how to navigate around this.
#this scriptincludes multuple error handling techniques to try and address various exceptions so as not to breat the script.

from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetmikoTimeoutException
from netmiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import SSHException


username = input('Enter your SSH username')
password = getpass()

with open('commands_file') as f: #commands to be executed.
    commands_list = f.read().splitlines()

with open('devices_file') as f: #IP addresses of the various devices, a file.
    devices_list = f.read().splitlines()

for devices in devices_list:  #this loop logs in to individual devices and executes the necessary commands
    print ('Connecting to device" ' + devices)
    ip_address_of_device = devices
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': 'username',
        'password': 'password'
    }

    try:
        net_connect = ConnectHandler(**ios_device)
    except (AuthenticationException):
        print('Authentication falilure: ' + ip_address_of_device)
        continue
    except (NetmikoTimeoutException):
        print('Timeout to the device: ' + ip_address_of_device)
        continue
    except (EOFError):
        print('End of file while attempting device: ' + ip_address_of_device)
        continue
    except (SSHException):
        print('SSH issue. Are you sure SSH is enabled: ' + ip_address_of_device)
        continue
    except Exception as unknown_error:
        print('some other error: ' + unknown_error)
        continue

    net_connect = ConnectHandler(**ios_device)
    output = net_connect.send_config_set(commands_list)
    print (output)