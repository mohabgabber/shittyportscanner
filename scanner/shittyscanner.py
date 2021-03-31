import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print('Invalid Amount Of Arguments')
    print("Syntax: python shittyscanner.py (Put The Ip Here)")
    print("Error Code: 0001")
    sys.exit()

print("-" * 50 )
print("Scanning Target: " + target)
print("Operation Started At: " + str(datetime.now()))
print("-" * 50 )

try:
    for port in range(0,100):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = s.connect_ex((target, port))
        print(f"[-] Checking Port Number: {port} \n")
        if result == 0:
            print(f"[Success] port {port} Is Open \n")
        s.close()
except KeyboardInterrupt:
    print("Exisiting Program")
    sys.exit()
except socket.gaierror:
    print("HostName Could Not Be Resolved")
    sys.exit()
except socket.error:
    print("Server Is Down")
    sys.exit()
