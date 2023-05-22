import binascii
import csv


headers =['42','4D','36','84','03','00','00','00','00','00','36','00','00','00','28','00','00','00',
'40','01','00','00','F0','00','00','00','01','00','18','00','00','00','00','00','00','84','03','00','C5','00',
'00','00','C5','00','00','00','00','00','00','00','00','00','00','00']


dir="2.BMP"
with open(dir,'rb') as img:
    hexdata = img.read().hex()
    hexlist = list(map(''.join, zip(*[iter(hexdata)]*2)))

hexArray=[]
for i in range(0,76800):
	data = hexlist[i]
	hexArray.extend([data,data,data])

with open('foto.BMP', 'wb') as f:
    f.write(binascii.unhexlify(''.join(headers)))
    f.write(binascii.unhexlify(''.join(hexArray)))
