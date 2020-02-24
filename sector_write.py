import os
def main(sektor):
    s=sektor
    if os.name == "nt":
        print(read_sector(r"\\.\physicaldrive0",s-1))
        wipe(r"\\.\physicaldrive0",s-1)
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(read_sector(r"\\.\physicaldrive0",s-1))
    else:
        print(read_sector("/dev/sdb",s-1))
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        wipe("/dev/sdb",s-1)
        print(read_sector("/dev/sdb",s-1))
def read_sector(disk, sector_no=0):
    f = open(disk, 'rb')
    f.seek(sector_no * 512)
    read = f.read(512)
    return read

def wipe(disk,sector_no=0):
    w= open(disk, 'wb')
    w.seek(sector_no*512)
    byte_arr = [0]
    binary_format = bytearray(byte_arr)
    for i in range(512):
        w.seek((sector_no*512)+i)
        w.write(binary_format)
    w.close()

if __name__ == "__main__":
    main(16) 
