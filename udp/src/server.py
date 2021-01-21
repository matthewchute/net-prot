import constants, helpers, os

temp_msg = None 
whole_msg = b''
file_path = None

helpers.sock.bind(constants.IP_PORT)

print "Server Ready"

# recieve 
while temp_msg != constants.EOF:
    datagram = helpers.sock.recvfrom(constants.BUFFER_SIZE)
    temp_msg = datagram[0]
    if file_path is None:
        print("Receiving " + temp_msg.decode() + "...")
        file_path = os.path.join(constants.SERVER_FILE_PATH, temp_msg.decode())
    else:
        whole_msg += temp_msg

whole_msg = whole_msg.strip(constants.EOF)

with open(file_path, 'wb') as sFile:
    sFile.write(whole_msg)

print "Received"
