import nmap

def scan_network(target):
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-sS -p 80,443')  # SYN scan

    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            print(f"Host: {host} is up")
            print(f"Open Ports on {host}:")
            for proto in nm[host].all_protocols():
                ports = nm[host][proto].keys()
                for port in ports:
                    print(f"Port: {port} - State: {nm[host][proto][port]['state']}")
        else:
            print(f"Host: {host} is down")


if __name__ =="__main__":
    target_ip="172.16.1.95/24"
    scan_network(target_ip)                          