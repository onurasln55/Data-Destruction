import os

def main(): 
    if os.name == "nt":
        print(read_sector(r"\\.\physicaldrive0"))
    else:
        print(read_sector("/dev/disk0"))

def read_sector(disk, sector_no=0):
    f = open(disk, 'rb')
    f.seek(sector_no * 512)
    read = f.read(512)
    return read

if __name__ == "__main__":
    main()
