import constants, socket 

sock = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

def sendDataGram(data): 
    """ to send datagram """
    if isinstance(data, str):
        data = str.encode(data)
    sock.sendto(data, constants.IP_PORT)