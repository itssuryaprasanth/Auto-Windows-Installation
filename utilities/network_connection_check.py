# Use this if you want to validate whether current network is reachable to your server or not.
import os
import sys


def connection_check_from_local_to_remote():
    hostname = "YOUR HOST"
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        print("VPN CONNECTION SUCCESSFULLY")
    else:
        sys.exit(1)


connection_check_from_local_to_remote()
