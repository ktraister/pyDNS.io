## SIMPLE IO DNS RESOLVER      

Simpleio.py takes any dns address, and returns an IP parsed out of the address. The operation is very similar to nip.io.  

EXAMPLE:
=======================================
(ins)[files][ssl]> dig @127.0.0.1 test.5.3.3.4.simple.io  

; <<>> DiG 9.10.6 <<>> @127.0.0.1 test.5.3.3.4.simple.io  
; (1 server found)  
;; global options: +cmd  
;; Got answer:  
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 12588  
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0  

;; QUESTION SECTION:  
;test.5.3.3.4.simple.io.	IN	A  

;; ANSWER SECTION:  
test.5.3.3.4.simple.io. 0	IN	A	5.3.3.4  

;; Query time: 0 msec  
;; SERVER: 127.0.0.1#53(127.0.0.1)  
;; WHEN: Tue Feb 05 15:22:59 EST 2019  
;; MSG SIZE  rcvd: 57  

