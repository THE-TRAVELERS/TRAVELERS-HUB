import socket

UDP_IP = "127.0.0.1" # "127.0.0.1" = loopback, par ailleurs on ne peut pas broadcast
UDP_PORT = 5005
MESSAGE = "1,2,3"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))