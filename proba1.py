import os

os.system('arp -d')
os.system('arp -a')
lines = os.popen('arp -a')
print (lines)