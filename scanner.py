import os

def checkPing(ip):
 response = os.system("ping -c 1 " + ip)
 if response == 0:
  return True
 else:
  return False

def scanNet(subnet):
 hosts = []
 for i in range(1, 255):
  addr = str(subnet) + "." + str(i)
  stat = checkPing(addr)
  if stat == True:
   hosts.append(addr)
 return hosts

def scanAgent(hosts):
 agents = []
 for i in hosts:
  stat = os.system("snmpget -v 2c -c public  " + i + " sysName.0")
  if stat == 0:
   agents.append(i)
 return agents

subnet = input("Enter subnet (i.e. 192.168.1):  ")

hosts = scanNet(subnet)
print("\nHosts in the subnet: \n")
print(hosts, "\n")

agents = scanAgent(hosts)
print("\nSNMP Agents: \n")
print(agents, "\n")
