#!/usr/bin/env python3


#"imported" list from file
my_list = [ "192.168.0.5", 5060, "UP" ]

#print the first item in the list (IP)
print("The first item in the list (IP): " + my_list[0] )

#printe the second item in the list (port)
print("The second item in the list (port): " + str(my_list[1]) )

#print the third item in the list (state)
print("The last item in the list (state): " + my_list[2] )

#second "imported" list
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

#print the data from the new list
print("The IP Addresses " + new_list[3] + " and " + new_list[4] + " are using the following ports and protocols: " + str(new_list[0]) + ", " + new_list[1] + ", " + str(new_list[2]) + ", " + new_list[5] + "." )




