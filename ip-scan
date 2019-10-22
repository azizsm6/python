import nmap

scanner = nmap.PortScanner()

print("Nmap Easy Scanner")

print("<------------------------->")


ip_x = input("Please Enter the IP address : ")
print("IP =====>  ", ip_x)
type(ip_x)

resp = input("""\nChoose what you want to scan
                1)SYN ACK Scan
                2)UDP Scan
                3)Comprehensive Scan""")
print("You have selected option: ", resp)

if resp == '1':
    print("Nmap Version:", scanner.nmap_version())
    scanner.scan(ip_x, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status:", scanner[ip_x].state())
    print(scanner[ip_x].all_protocols())
    print("Open Ports: ", scanner[ip_x]['tcp'].keys())
    
