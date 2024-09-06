import nmap

def scan_host(ip_address, output_file="nmap_scan_results.txt"):
    """
    Function to perform Nmap scan and write results to a file.
    Args:
        ip_address (str): The IP address of the target.
        output_file (str): The file to save the results.
    """
    # Create an Nmap PortScanner object
    nm = nmap.PortScanner()
    
    # Perform the scan
    print(f"Scanning {ip_address}...")
    nm.scan(ip_address, arguments="-sV -O --script vuln")
    
    # Open the output file in write mode
    with open(output_file, "w") as f:
        # Write scan summary
        f.write(f"Nmap Scan Report for {ip_address}\n")
        f.write("="*50 + "\n")
        
        # Get open ports and services
        f.write("Open Ports and Services:\n")
        for protocol in nm[ip_address].all_protocols():
            ports = nm[ip_address][protocol].keys()
            for port in ports:
                service = nm[ip_address][protocol][port]
                f.write(f"Port: {port}\tService: {service['name']}\tVersion: {service.get('version', 'N/A')}\n")
        f.write("\n")
        
        # Get OS detection
        if "osmatch" in nm[ip_address]:
            f.write("Operating System Detection:\n")
            for os in nm[ip_address]["osmatch"]:
                f.write(f"OS: {os['name']} (Accuracy: {os['accuracy']}%)\n")
        f.write("\n")
        
        # Get device type
        if "osclass" in nm[ip_address]:
            f.write("Device Type:\n")
            for osclass in nm[ip_address]["osclass"]:
                f.write(f"Device Type: {osclass['type']} (Accuracy: {osclass['accuracy']}%)\n")
        f.write("\n")
        
        # Get Hostnames
        if "hostnames" in nm[ip_address]:
            f.write("Hostnames:\n")
            for hostname in nm[ip_address]["hostnames"]:
                f.write(f"Hostname: {hostname['name']} ({hostname['type']})\n")
        f.write("\n")
        
        # Get Network Interfaces and IPs
        if "addresses" in nm[ip_address]:
            f.write("Network Interfaces and IPs:\n")
            for addr_type, addr in nm[ip_address]["addresses"].items():
                f.write(f"{addr_type}: {addr}\n")
        f.write("\n")
        
        # Get Scripts and Vulnerabilities
        if "script" in nm[ip_address]:
            f.write("Script Outputs and Vulnerabilities:\n")
            for script_id, output in nm[ip_address]["script"].items():
                f.write(f"Script: {script_id}\n{output}\n\n")
        
        print(f"Scan results saved to {output_file}")
