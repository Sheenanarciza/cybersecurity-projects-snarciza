import nmap  # Import the nmap module to interact with Nmap for network scanning

# Define the range of ports to scan
begin = 75  # Starting port number for scanning (adjust as needed)
end = 80  # Ending port number for scanning (adjust as needed)

# Specify the target IP address or domain here (e.g., '192.168.1.1')
target = "127.0.0.1"  # Replace with your target

# Initialize the Nmap PortScanner object
scanner = nmap.PortScanner()

# Loop through the range of port numbers to scan (from 'begin' to 'end', inclusive)
for i in range(begin, end+1):
    # Perform the scan on the target and current port number 'i'
    res = scanner.scan(target, str(i))
    # Access the scan results and get the state (open/closed) of the port
    res = res['scan'][target]['tcp'][i]['state']
    #tcp [i] iterater 

    # Print the result for the current port
    print(f'Port {i} is {res}.')  # Output the status of the port (open or closed)
