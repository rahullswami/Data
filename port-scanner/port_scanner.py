import re
from colorama import Fore
import time
import pyfiglet
import socket
import threading

def check_ip_and_scan_ports(ip_address, start_port, end_port):
    ipv4_pattern = r'^((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'
    ipv6_pattern = r'^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$'

    if re.match(ipv4_pattern, ip_address):
        print(pyfiglet.figlet_format('IPv4'))
        print(f"{Fore.GREEN}IPv4 ======>", ip_address)
    elif re.match(ipv6_pattern, ip_address):
        print(pyfiglet.figlet_format('IPv6'))
        print(f"{Fore.GREEN}IPv6 ======>", ip_address)
    else:
        print(f"{Fore.RED}Invalid IP address")
        return

    try:
        target = socket.gethostbyname(ip_address)
    except socket.gaierror:
        print('Name resolution error')
        return

    print('Scanning target', target)
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        thread.start()

def scan_port(target, port):
    #print('Scanning port', port)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(3)
        conn = s.connect_ex((target, port))
        if not conn:
            print(f'{Fore.BLUE}Port {port} is open')

start_port = int(input(f'{Fore.GREEN}Enter start port: '))
end_port = int(input(f'{Fore.GREEN}Enter end port: '))
ip_address = input(f'{Fore.GREEN}Enter IP address: ')

check_ip_and_scan_ports(ip_address, start_port, end_port)
