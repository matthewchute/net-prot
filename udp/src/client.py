import constants, helpers, os, sys

file_name = sys.argv[1]
file_path = constants.CLIENT_FILE_PATH + "/" + file_name

# send file name first
helpers.sendDataGram(file_name)

# send
with open(file_path, "rb") as cFile:
    print("Sending " + file_name + "...")
    datagram = cFile.read(constants.BUFFER_SIZE)
    while datagram:
        helpers.sendDataGram(datagram)
        datagram = cFile.read(constants.BUFFER_SIZE)

helpers.sendDataGram(constants.EOF)

print "Sent"
