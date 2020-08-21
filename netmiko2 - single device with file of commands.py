from netmiko import ConnectHandler

with open('commands_file') as f: #a list of command files to be read and executed by this script.
    commands_to_send = f.read().splitlines()

ios_devices = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.72',
    'username': 'astra',
    'password': 'cisco',
}

all_devices = [ios_devices] #we could add more dicts and increase the number of devices to connect to

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(commands_to_send) #list of commands executed, you can add as many as possible.
    print (output) 