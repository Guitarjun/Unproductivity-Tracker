import os
from shutil import copyfile
import argparse

backup = 'hosts - Backup'
working_dir = os.getcwd()

# List of URLs to block/unblock
sites_to_block = []

# Path to 'hosts' file in Windows folder
hosts_folder = 'C:/Windows/System32/drivers/etc/'

hosts_path = hosts_folder + 'hosts'

redirect = "127.0.0.1"  # Local host (make sure you are not running a local server while using this script)

# Set up arg parser
parser = argparse.ArgumentParser(description='block or unblock sites')
parser.add_argument('-b', '--block', action='store_true')
parser.add_argument('-u', '--unblock', action='store_true')
args = parser.parse_args()


def block_websites() -> None:
    if args.block:
        print("Blocking sites...")
        with open(hosts_path, 'r+') as hostfile:
            hosts_content = hostfile.read()
            for site in sites_to_block:
                if site not in hosts_content:
                    hostfile.write(redirect + ' ' + site + '\n')
    elif args.unblock:
        print('Unblocking sites...')
        with open(hosts_path, 'r+') as hostfile:
            lines = hostfile.readlines()
            hostfile.seek(0)
            for line in lines:
                if not any(site in line for site in sites_to_block):
                    hostfile.write(line)
            hostfile.truncate()


def create_backup() -> None:
    current_files = os.listdir(hosts_folder)
    if backup not in current_files:
        print('creating backup')
        copyfile(hosts_path, hosts_folder + backup)


# sudo python blocker.py
if __name__ == '__main__':
    create_backup()
    block_websites()
