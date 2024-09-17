from netmiko import ConnectHandler 
from datetime import datetime

# Switch details
switches = [
    {
        'device_type': 'cisco_ios_telnet',
        'host': '10.10.10.1',
        'username': 'admin',
        'password': 'XXXXXXX',
        'secret': 'XXXXXXX',
    },
    {
        'device_type': 'cisco_ios_telnet',
        'host': '10.10.10.3',
        'username': 'admin',
        'password': 'XXXXXXX',
        'secret': 'XXXXXXX',
    },
    {
        'device_type': 'cisco_ios_telnet',
        'host': '10.10.10.5',
        'username': 'admin',
        'password': 'XXXXXXX',
        'secret': 'XXXXXXX',
    },
    {
        'device_type': 'cisco_ios_telnet',
        'host': '10.10.10.6',
        'username': 'admin',
        'password': 'XXXXXXX',
        'secret': 'XXXXXXX',
    },
    {
        'device_type': 'cisco_ios_telnet',
        'host': '10.10.10.7',
        'username': 'admin',
        'password': 'XXXXXXX',
        'secret': 'XXXXXXX',
    },
    {
        'device_type': 'cisco_ios_telnet',
        'host': '10.10.10.8',
        'username': 'admin',
        'password': 'XXXXXXX',
        'secret': 'XXXXXXX',
    },
    {
        'device_type': 'cisco_ios_telnet',
        'host': '10.10.10.9',
        'username': 'admin',
        'password': 'XXXXXXX',
        'secret': 'XXXXXXX',
    },
    {
        'device_type': 'cisco_ios_telnet',
        'host': '192.168.10.13',
        'username': 'admin',
        'password': 'XXXXXXX',
        'secret': 'XXXXXXX',
    },
    {
        'device_type': 'cisco_ios_telnet',
        'host': '192.168.10.14',
        'username': 'admin',
        'password': 'XXXXXXX',
        'secret': 'XXXXXXX',
    },
    {
        'device_type': 'cisco_ios_telnet',
        'host': '192.168.10.15',
        'username': 'admin',
        'password': 'XXXXXXX',
        'secret': 'XXXXXXX',
    },
    {
        'device_type': 'cisco_ios_telnet',
        'host': '192.168.10.18',
        'username': 'admin',
        'password': 'XXXXXXX',
        'secret': 'XXXXXXX',
    },
]

# Backup filenames
current_date = datetime.now().strftime("%Y-%m-%d")

# Backup configuration
def backup_running_config(switch):
    try:
        # Connecting switch
        connection = ConnectHandler(**switch)
        print(f"Connected to {switch['host']}")

        # Enter enable mode
        connection.enable()
        print(f"Entered enable mode on {switch['host']}")

        # show running-config 
        running_config = connection.send_command('show running-config')

        # Backup file name
        filename = f"{switch['host']}_running_config_{current_date}.txt"

        # Save text file
        with open(filename, 'w') as config_file:
            config_file.write(running_config)

        print(f"Backup of {switch['host']} saved to {filename}")
        connection.disconnect()
    except Exception as e:
        print(f"An error occurred with {switch['host']}: {str(e)}")

# Loop each switch
for switch in switches:
    backup_running_config(switch)

print("Backup process completed!")
