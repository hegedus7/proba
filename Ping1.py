from scapy.all import sniff

def packet_callback(packet):
    print(packet.show())

sniff(prn=packet_callback, store=0)



