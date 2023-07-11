# Network Scanner

**WPROWADZENIE**

Celem projektu było stworzenie skanera, który przeskanuje sieć w poszukiwaniu aktywnych hostów i agentów SNMP.
Program został napisany w języku Python i uruchomiony w systemie Ubuntu 20.04.1 LTS.
Projekt zrealizowano w ramach przedmiotu uniwersyteckiego "Signalling and Management System".

**FUNKCJONALNOŚĆ**

Po uruchomieniu program najpierw prosi użytkownika o podanie podsieci w postaci „192.168.1”, a następnie skanuje sieć w poszukiwaniu aktywnych hostów funkcją _scanNet()_.
Skanowanie jest wykonywane poprzez pingowanie adresów z określonej podsieci, zaczynając od 1 do 254, przy użyciu zdefiniowanej funkcji _checkPing()_. Adresy, które odpowiadają, są dodawane do listy.
Następnie adresy z tej listy są skanowane w poszukiwaniu włączonych agentów SNMP. Służy do tego funkcja _scanAgent()_. 
Funkcja polega na wysłaniu żądania do hosta i jeśli otrzyma od niego odpowiedź, oznacza to, że ma włączonego agenta SNMP. <br/>
Na koniec program zwraca 2 listy: <br/>
- z aktywnymi hostami <br/>
- z hostami z włączonym agentem SNMP.


**URUCHOMIENIE PROGRAMU**

W celu uruchomienia skanera zalecam użycie Pythona 3.0.

`$ python3 scanner.py`

# --- ENGLISH VERSION ---
**INTRODUCTION**

The aim of the project was to create a scanner that will scan the network for active hosts and SNMP agents.
The program was written in Python language and was run on Ubuntu 20.04.1 LTS.
The project was implemented as part of the university course "Signalling and Management System".

**FUNCTIONALITY**

After launching the program first asks the user to enter the subnet in the form "192.168.1" and then scans the network for active hosts with the _scanNet()_ function.
This scan is done by pinging addresses from a specific subnet, starting from 1 to 254, using the defined _checkPing()_ function. Addresses that respond are added to the list.
Then addresses from the list are scanned for enabled SNMP agents. The _scanAgent()_ function is used for this.
The function is to send a request to the host and if it gets response from it, it means that it has the SNMP agent enabled.  <br/>
Finally, the program returns 2 lists: <br/>
-> with active hosts <br/>
-> with hosts with SNMP agent enabled.

**LAUNCHING THE PROGRAM**

I recommend using Python 3.0 to run the scanner. 

`$ python3 scanner.py`
