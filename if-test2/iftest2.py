#!/usr/bin/env python3

from ipaddress import ip_address, IPv4Address, IPv6Address

ipchk = input('Apply an IP address: ') # this line now prompts the user for input

ipchk = ip_address(ipchk)
print(ipchk)
print(type(ipchk))

if ipchk == '192.168.70.1': # if a match on '192.168.70.1'
   # indented under if
   print('Looks like the IP address of the Gateway was set: ' + ipchk + ' This is not recommended.')

elif ipchk: # if any data is provided, this will test true
    if type(ip_address(ipchk)) == IPv4Address:
        print('Looks like the IP address was set: ' + ipchk) # indented under if
    else:
        print('You did not provide a valid IPv4 Address.')

else: # if data is NOT provided
   print('You did not provide input.') # indented under else
