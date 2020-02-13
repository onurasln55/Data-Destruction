import os
def end_sector(disk):
    os.system("fdisk -l %s >fdisk.lst"%disk)
    with open("fdisk.lst") as file:
        dosya=file.read()
        #print(dosya)
        dosya=dosya.split()
        #print(dosya)
        j=0
        for i in dosya:
            j=j+1
        for i in range(j):
            if dosya[i]=="sektör":
                #print(int(dosya[i-1]))
                max_sector=int(dosya[i-1])
        for i in range(j):
            if dosya[i]=="=" and dosya[i-1]==dosya[i+1]:
                #print(dosya[i+1])
                sector_size=int(dosya[i+1])

    return max_sector,sector_size

dizi=end_sector("/dev/sda")
print(dizi)
