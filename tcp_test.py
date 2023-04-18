#!/usr/bin/env python
import argparse
import sys
import socket
import random
import struct

from scapy.all import sendp, send, get_if_list, get_if_hwaddr
from scapy.all import Packet
from scapy.all import Ether, IP, UDP, TCP

def get_if():
    ifs=get_if_list()
    iface=None # "h1-eth0"
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break
    if not iface:
        print("Cannot find eth0 interface")
        exit(1)
    return iface

def main():

    # if len(sys.argv)<3:
    #     print 'pass 2 arguments: <destination> "<message>"'
    #     exit(1)

    addr = "192.168.1.52"
    iface = "wlan0"
    payload = "--Info--\nCPU Usage:100%;\nTemperature: 90°;\nHumidity: 50%;"

    print("sending on interface %s to %s" % (iface, str(addr)))
    
    pkt = Ether(src=get_if_hwaddr(iface), dst='ff:ff:ff:ff:ff:ff')
    pkt = IP(dst="192.168.56.101")/TCP(dport=8082, sport=random.randint(49152,65535))/payload
    pkt.show2()
    send(pkt)


if __name__ == '__main__':
    main()

