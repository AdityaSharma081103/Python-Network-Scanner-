import socket 
from scapy.all import IP , ICMP, sr
import nmap
def display_menu():
    print("\n Python Network Scanner")
    print("----------------------------------------- ")
    print(" 1. Port scan using Socket")
    print(" 2. Ping sweep using Scapy")
    print(" 3. port sacn using nmap ")
    print(" 0. EXIT")
    print("" \
    "---------------------------------------")


#import socket 
def check_host(ip , port):
    try:
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        #socket.AF_INET = used standred IPV4 protocol
        #socket.SOCK_STREAM = used TCP stream

        s.settimeout(1)
        #socket.settimeout() = set time for socket's operations 

        result = s.connect_ex ((ip , port))
        # socket.connect_ex = attempts to connect to the specified ip and port 

        if result ==0:
            print(f"HOST {ip} is UP on port {port}")
        else:
            print(f"HOST {ip} is DOWN on port {port}")
            socket.close()

    except Exception as e :
        print(f"ERROR : {e}")        


def ping_sweep(network):
     answered , _ = sr(IP(dst=network)/ICMP(), timeout=2, verbose=False)
     for sent, received in answered:
      print(f"Host {received.src} is UP")



def portscannmap(ip_add,port_no):
    nm = nmap.PortScanner()
    nm.scan(ip_add,port_no)
    for host in nm.all_hosts():
        print(f"Host:{host}({nm[host].hostname()})")
        print(f"state:{nm[host].state()}")

        for proto in nm[host].all_protocols():
            print(f"________________________")
            print(f"Protocal:{proto}")
            lport = nm[host][proto].keys()

            for port in lport:
                state=nm[host][proto][port]['state']
                service=nm[host][proto][port]['name']
                version=nm[host][proto][port]['version']
                print(f"port:{port} \t state: {state} \t service:{service} \t version: {version}")


def main():
    while True:
        display_menu()
        choice = input("Enter Your choice (0-3) : ")
        

        if choice == "1" : 
            print("you have Selected : Port Scan using Socket")
            check_host((input("Enter Target IP -->")), (int(input("Enter Target Port -->"))))

        elif choice == "2":
            print("you have Selected Ping Sweep using Scapy")
            ping_sweep(input("Enter Target IP -->"))
        elif choice == "3":
            print("You have Selected port Scan using Nmap ")
            portscannmap(input("Enter Target IP -->"), (input("Enter Target Port -->")))

        elif choice == "0":
            print("You have been Exit")
            break

        else :
            print("Enter other number ")

if __name__=="__main__":
    main()