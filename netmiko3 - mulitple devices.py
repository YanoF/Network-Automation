from netmiko import ConnectHandler

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
        'username': 'astra',
        'password': 'cisco'
    }

    net_connect = ConnectHandler(**ios_device)
    output = net_connect.send_config_set(commands_list)
    print (output)
