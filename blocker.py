from datetime import datetime
import json
import os
from shutil import copyfile

backup = 'hosts - Backup'
working_dir = os.getcwd()

end_time = datetime(2023, 1, 1, 20)  # y, m, d, h, min

sites_to_block = ['www.facebook.com', 'facebook.com']
sites = {'Facebook': ['www.facebook.com', 'facebook.com'], 'YouTube': ['www.youtube.com']}  # Get this from JSON file

# Path to 'hosts' file in Windows folder
hosts_folder = 'C:/Windows/System32/drivers/etc/'
hosts_path = hosts_folder + 'hosts'

redirect = "127.0.0.1"  # Local host (make sure you are not running a local server while using this script)


def block_websites() -> None:
    if datetime.now() < end_time:
        print("Block sites")
        with open(hosts_path, 'r+') as hostfile:
            hosts_content = hostfile.read()
            for site in sites_to_block:
                if site not in hosts_content:
                    hostfile.write(redirect + ' ' + site + '\n')
    else:
        print('Unblock sites')
        with open(hosts_path, 'r+') as hostfile:
            lines = hostfile.readlines()
            hostfile.seek(0)
            for line in lines:
                if not any(site in line for site in sites_to_block):
                    hostfile.write(line)
            hostfile.truncate()


def create_backup():
    current_files = os.listdir(hosts_folder)
    if backup not in current_files:
        print('creating backup')
        copyfile(hosts_path, hosts_folder + backup)

# sudo python blocker.py
if __name__ == '__main__':
    create_backup()
    block_websites()
