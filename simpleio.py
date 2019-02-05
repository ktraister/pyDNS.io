import socket
import dnslib

UDP_IP = "127.0.0.1"
UDP_PORT = 53

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

def isint(INTEGER):
    try:
        int(INTEGER)
        return True
    except:
        return False

while True:
    try:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        myreq = dnslib.DNSRecord.parse(data)
        print("------START------")
        print("RECEIVED MESSAGE --> ", myreq)
        print("^^^ FROM ADDRESS --> ", addr)
        for line in str(myreq).split("\n"):
            if "id:" in line:
                request = line.split(' ')[7].replace(';', '')
                print("REQUEST_ID: ", request)
                break

        for line in str(myreq).split("\n"):
            if ".dominos.io" in line:
                inreq = line.split(' ')[0].replace(';', '') 
                returnaddr = []
                for line in inreq.split('.'):
                    if isint(line):
                        returnaddr.append(str(line)+".")

        if len(returnaddr) > 4:
            returnaddr = returnaddr[:4]

        addrstring = ''.join(e for e in returnaddr)
        print("RETURNING IP ", addrstring[:len(addrstring)-1])
        d = dnslib.DNSRecord(dnslib.DNSHeader(id=int(request),qr=1,aa=1,ra=1), q = dnslib.DNSQuestion(inreq), a = dnslib.RR(inreq,rdata=dnslib.A(addrstring[:len(addrstring)-1])))

        sock.sendto(d.pack(), addr)
        print("======END=======")
        print()
    except Exception as e:
        print()
        print("FAILURE IN PARSER: ", e)
        print()

    
