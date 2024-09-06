from nmap_scanner.scanner import scan_host

if __name__ == "__main__":
    # Take IP address input from the user
    ip_address = input("Enter the IP address to scan: ")
    output_file = "nmap_scan_results.txt"
    
    # Perform the scan and save results to the text file
    try:
        scan_host(ip_address, output_file)
    except Exception as e:
        print(f"An error occurred: {e}")

