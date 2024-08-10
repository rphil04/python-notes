import scapy.all as scapy
import socket
import json
import os
import subprocess

# Directory and file to store previous scan results
SCAN_DIRECTORY = '/home/scans'
PREVIOUS_SCAN_FILE = os.path.join(SCAN_DIRECTORY, 'previous_scan.json')

# Ensure the scan directory exists
os.makedirs(SCAN_DIRECTORY, exist_ok=True)


def scan_network(ip_range):
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    devices = []
    for element in answered_list:
        ip = element[1].psrc
        mac = element[1].hwsrc
        hostname = get_hostname(ip) or get_netbios_name(ip) or 'Unknown'
        devices.append({"ip": ip, "mac": mac, "hostname": hostname})

    return devices


def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return None


def get_netbios_name(ip):
    try:
        output = subprocess.check_output(['nbtscan', '-v', ip], stderr=subprocess.DEVNULL)
        for line in output.splitlines():
            if b'Name=' in line:
                return line.split(b'Name=')[1].split(b'<')[0].decode('utf-8').strip()
    except subprocess.CalledProcessError:
        pass
    return None


def load_previous_scan():
    if os.path.exists(PREVIOUS_SCAN_FILE):
        with open(PREVIOUS_SCAN_FILE, 'r') as file:
            return json.load(file)
    return []


def save_current_scan(current_scan):
    with open(PREVIOUS_SCAN_FILE, 'w') as file:
        json.dump(current_scan, file, indent=4)


def compare_scans(previous_scan, current_scan):
    previous_ips = {device["ip"] for device in previous_scan}
    current_ips = {device["ip"] for device in current_scan}

    new_devices = [device for device in current_scan if device["ip"] not in previous_ips]
    removed_devices = [device for device in previous_scan if device["ip"] not in current_ips]

    return new_devices, removed_devices


def display_devices(devices, label):
    print(f"\n{label}:")
    for device in devices:
        print(f"IP: {device['ip']}, MAC: {device['mac']}, Hostname: {device['hostname']}")


if __name__ == "__main__":
    # Define the IP range for your network
    ip_range = "192.168.0.1/24"

    print("Scanning network...")
    current_scan = scan_network(ip_range)

    previous_scan = load_previous_scan()
    new_devices, removed_devices = compare_scans(previous_scan, current_scan)

    display_devices(current_scan, "Current Devices")
    display_devices(new_devices, "New Devices")
    display_devices(removed_devices, "Removed Devices")

    save_current_scan(current_scan)
    print(f"\nScan completed and saved to {PREVIOUS_SCAN_FILE}.")
