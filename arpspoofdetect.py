import os
from datetime import datetime
import socket

host = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[1] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
ipMAC = {}

def arp_ex():
    try:
        os.system(f'arp -a -N {host} | grep -v "ff-ff-ff-ff-ff-ff" > arp.txt') #this is for windows machine that has grep installed
        with open('arp.txt', 'r') as arp:                                      # use 'ff:ff:ff:ff:ff:ff' and remove '-N' switch for linux
            for i in arp.readlines():
                if 'static' in i or 'dynamic' in i:
                    i = i.split()
                    ipMAC[i[0]] = i[1]
    except Exception as e:
        print(e)
    finally:
        return ipMAC
arp_ex()

rev_dict = {}
def MAC_dup():
    for key, value in ipMAC.items():
        rev_dict.setdefault(value, set()).add(key)
    result = [key for key, values in rev_dict.items() if len(values) > 1]
    return result

def main():
    if MAC_dup() > []:
        try:
            current_time = datetime.now()
            with open('log.txt', 'a') as log:
                log.write(f"\nArp spoofed!\nThe address is: {MAC_dup()}\nDate: {current_time}\n")
                log.close()
        except:
            print("Error")
    else:
        print("No spoofing attacks detected!")

if __name__ == '__main__':
    main()

# run below commands on attacker machine as root
# echo 1 > /proc/sys/net/ipv4/ip_forward
# arp -i eth0 -t <target> <gateway>
