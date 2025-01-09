#note - script did not work, need to review

import nmap
# Import the nmap modules or librarie (that are bigger collections of code) to interact with Nmap for network scanning
# adds additional functionality to our script that we are providing

nm = nmap.PortScanner()
# Create an instance of the PortScanner class to initiate scanning

target = " "
# The target IP address or hostname (replace with the actual target)
options = "-sV -sC scan_results"
# The target IP address or hostname (replace with the actual target)
# -sC means I want to run a standard math script

nm.scan(target, arguments=options)
# is calling scan method on the target with the specified options

# Loop through all hosts found in the scan
for host in nm.all_hosts():
    print("host: %s (%s)" % (host, nm[host].hostname()))
    # Loop through all hosts found in the scan
    print("State: %s" % nm[host].state())
     # Print the state (up or down) of the host

      # Loop through all protocols found on the host (usually tcp or udp)
    for protocol in nm[host].all_protocols():
          print("Protocol: %s" % protocol)  # Print the protocol (TCP, UDP, etc.)
          port_info = nm[host][protocol]  # Retrieve port information for the given protocol
          for port, state in port_info.items(): # Loop through all ports found for that protocol
            print("Port: %s\tState: %s" % (port, state)) # Print port number and its state (open, closed, etc.)
