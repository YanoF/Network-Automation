#this scripts connects to the device and returns the show ip int br

from getpass import getpass
from netmiko import ConnectHandler

username = input('Enter your SSH username: ')
password = getpass()

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': username,
    'password': password,
}

net_connect = ConnectHandler(**iosv_l2_s1)
output = net_connect.send_command('show ip int brief')
print(output)

