import socket

ip_addr = input("Please enter an IP Address: ")
try:
    socket.inet_aton(ip_addr)
    print("You have input a valid IP Address")
except socket.error:
    print("Invalid IP Address Please try again")

