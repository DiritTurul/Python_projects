import subprocess
import time
import random
import pyfiglet

def ping_ip(ip_address):
    try:
        while True:
            response = subprocess.run(
                ["ping", "-c", "1", ip_address],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            if response.returncode == 0:
                print(f"Ping to {ip_address} successful.")
            else:
                print(f"Ping to {ip_address} failed.")
            
    except KeyboardInterrupt:
        print("Ping process interrupted by user.")

def main():
    ascii_banner = pyfiglet.figlet_format("DOS_by_ping")
    print(ascii_banner)
    i = random.randint(0,1)
    if i in range(0,1):
        ping_ip("IP")  
    else:
        ping_ip("IP")
main()