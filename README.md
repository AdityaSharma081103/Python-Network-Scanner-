#Python Network Scanner

A simple Python tool to learn network scanning. It has 3 options:
Socket Port Scan – check if a port is open.
Scapy Ping Sweep – find live hosts with ICMP.
Nmap Scan – show open ports, services, and versions.


⚠️ Use only on networks you own or have permission to test.

Requirements
Python 3.8+
scapy
python-nmap
nmap installed on system

Install: 
pip install scapy python-nmap

Usage

Run: 
python3 scanner.py

Follow the menu to choose:
1: Port scan with socket
2: Ping sweep with scapy
3: Port scan with nmap
0: Exit

Example: Enter Your choice (0-3) : 2 
         Enter Target IP --> 192.168.1.0/24
         Host 192.168.1.1 is UP
