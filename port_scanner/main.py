import pyfiglet
import sys
import socket 
from datetime import datetime

# for header 
ascii_banner = pyfiglet.figlet_format("Machine_Scaning")
print(ascii_banner)

# input for target ip add
target =input(str("Target IP : "))

#banner 
print("_"*50)
print("scanning target : " + target)
print("scanning started at " + str(datetime.now()))
print("_"*50)

try:
    
    #scan every port on ip 
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        
        #return open port 
        result = s.connect_ex((target,port))
        if result == 0 :
          print("[*] port {} is open ".format(port))
        s.close()
        
except KeyboardInterrupt :
    print("\n Exiting : ")
    sys.exit()
    
except socket.error:
    print("\  host not responding : ")
    sys.exit()