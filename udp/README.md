## Purpose   
Use UDP to transfer a file from a client to a server.   

## Running the code:  
You will need two shells. One will act as the server and the other will act as the client.  

Run the server code first from src:  
`python server.py`    

Next run the client code from src while also passing the name of the file you would like to transfer:    
`python client.py test.txt`  

After running you should notice the file sent from client's assets should appear in the server's assets.  