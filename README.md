
# Network Scanner

**INTRODUCTION:**

The aim of the project was to create a scanner that will scan the network for active hosts and SNMP agents. <br/>
The program was written in Python language and was run on Ubuntu 20.04.1 LTS.

**FUNCTIONALITY:**

After launching the program first asks the user to enter the subnet in the form "192.168.1" and then scans the network for active hosts with the "scanNet()" function.  <br/> 
This scan is done by pinging addresses from a specific subnet, starting from 1 to 254, using the defined checkPing() function. Addresses that respond are added to the list.  <br/>
Then addresses from the list are scanned for enabled SNMP agents. The "scanAgent()" function is used for this.  <br/>
The function is to send a request to the host and if it gets response from it, it means that it has the SNMP agent enabled.  <br/>
Finally, the program returns 2 lists: <br/>
-> with active hosts <br/>
-> with hosts with SNMP agent enabled.

**LAUNCHING THE PROGRAM:**

I recommend using Python 3.0 to run the scanner. 

`$ python3 scanner.py`
