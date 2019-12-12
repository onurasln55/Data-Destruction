import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import os

# --- functions ---

def page1():

    labels["2"].pack_forget()
    labels["3"].pack_forget()
    labels["4"].pack_forget()

    buttons["1"].pack_forget()
    buttons["11"].pack_forget()
    buttons["2"].pack(side=tk.BOTTOM,anchor=tk.SE)
    buttons["22"].pack_forget()
    buttons["3"].pack_forget()
    buttons["33"].pack_forget()
    buttons["4"].pack_forget()
    listbox.pack_forget()
    buttons["yenile"].pack_forget()

def page2():
    labels["2"].pack()
    labels["3"].pack_forget()
    labels["4"].pack_forget()

    buttons["1"].pack_forget()
    buttons["11"].pack(side=tk.RIGHT,anchor=tk.S)
    buttons["2"].pack_forget()
    buttons["22"].pack_forget()
    buttons["3"].pack(side=tk.RIGHT,anchor=tk.S)
    buttons["4"].pack_forget()
    buttons["yenile"].pack(side=tk.RIGHT,anchor=tk.S)
    listbox.pack(side=tk.LEFT,anchor=tk.S)
    refresh()


def page3():
    labels["2"].pack_forget()
    labels["3"].pack()
    labels["4"].pack_forget()

    buttons["1"].pack_forget()
    buttons["11"].pack_forget()
    buttons["2"].pack_forget()
    buttons["22"].pack(side=tk.BOTTOM,anchor=tk.SE)
    buttons["3"].pack_forget()
    buttons["4"].pack(side=tk.BOTTOM,anchor=tk.SE)
    buttons["yenile"].pack_forget()
    listbox.pack_forget()


def page4():
    labels["2"].pack_forget()
    labels["3"].pack_forget()
    labels["4"].pack()

    buttons["1"].pack_forget()
    buttons["11"].pack_forget()
    buttons["2"].pack_forget()
    buttons["22"].pack_forget()
    buttons["3"].pack_forget()
    buttons["33"].pack_forget()
    buttons["4"].pack_forget()
    buttons["5"].pack(side=tk.BOTTOM,anchor=tk.SE)
    buttons["yenile"].pack_forget()
    listbox.pack_forget()
def refresh():
    listbox.delete(0,tk.END)
    os.system('lsblk /dev/sd* --nodeps --output NAME,MODEL,VENDOR,SIZE,TYPE,STATE >disk.lst')
    liste=open("disk.lst","r")
    liste=liste.readlines()
    for disk in liste:
        if "running" in disk:
            disk=disk.replace('\n','')
            disk=disk.replace("running","Çalışıyor")
            disk=disk.replace("disk","")
            listbox.insert(tk.END,disk)


# --- main ---

root = tk.Tk()
# root.attributes('-fullscreen',True)
# lisans=tk.Entry(root)#lisans girdisi

func = {  # sayfalar için fonksiyon
    "1": page1,
    "2": page2,
    "3": page3,
    "4": page4,
    "yenile":refresh,

}

buttons = {  # butonlar için fonksiyonlar
    "1": tk.Button(root, text="Sonraki ", command=func["1"]),
    "11": tk.Button(root, text="Önceki", command=func["1"]),
    "2": tk.Button(root, text="Sonraki", command=func["2"]),
    "22": tk.Button(root, text="Önceki", command=func["2"]),
    "3": tk.Button(root, text="Sonraki ", command=func["3"]),
    "33": tk.Button(root, text="Önceki", command=func["3"]),
    "4": tk.Button(root, text="Sonraki ", command=func["4"]),
    "5": tk.Button(root, text="Çıkış", command=quit),
    "yenile": tk.Button(root, text="Yenile ", command=func["yenile"]),
}

labels = {
    "başlık": tk.Label(root, text="PROWIPE", font=("Arial Bold", 50)),
    "2": tk.Label(root, text="Disk Seçin ve imha edin"),
    "3": tk.Label(root, text="İmha işlemi sürüyor... "),
    "4": tk.Label(root, text="İşlem Tamam"),
}
pgbar=Progressbar(root,length=200,orient=HORIZONTAL,maximum=100,value=0)
labels["başlık"].pack(expand=YES,fill=BOTH)
listbox = tk.Listbox(root,width=50)

buttons["2"].pack()
root.mainloop()
