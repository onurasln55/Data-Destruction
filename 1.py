import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import os
from filehash import FileHash


import apply as apply

##pages start
def page1():
    labels["2"].pack_forget()
    labels["3"].pack_forget()
    labels["4"].pack_forget()
    anasol.pack_forget()
    anasag.pack_forget()
    mlb.pack_forget()
    buttons["1"].pack_forget()
    buttons["11"].pack_forget()
    buttons["2"].pack(side=tk.BOTTOM,anchor=tk.SE)
    buttons["22"].pack_forget()
    buttons["3"].pack_forget()
    buttons["33"].pack_forget()
    buttons["4"].pack_forget()
def page2():
    labels["2"].pack()
    labels["3"].pack_forget()
    labels["4"].pack_forget()
    anasol.pack(side=LEFT)
    anasag.pack(side=RIGHT)
    info.pack()
    mlb.pack(expand=YES, fill=BOTH)

    buttons["1"].pack_forget()
    buttons["2"].pack_forget()
    buttons["22"].pack_forget()
    buttons["3"].pack()
    buttons["11"].pack()
    buttons["4"].pack_forget()
    refresh()
    smart_info()

def page3():
    labels["2"].pack_forget()
    labels["3"].pack()
    labels["4"].pack_forget()
    mlb.pack_forget()
    info.pack_forget()
    Label(root,text=mlb.get(disk)).pack()
    anasol.pack_forget()
    anasag.pack_forget()
    buttons["1"].pack_forget()
    buttons["11"].pack_forget()
    buttons["2"].pack_forget()
    buttons["22"].pack(side=tk.BOTTOM,anchor=tk.SE)
    buttons["3"].pack_forget()
    buttons["4"].pack(side=tk.BOTTOM,anchor=tk.SE)

def page4():
    labels["2"].pack_forget()
    labels["3"].pack_forget()
    labels["4"].pack()
    anasol.pack_forget()
    anasag.pack_forget()
    mlb.pack_forget()
    buttons["1"].pack_forget()
    buttons["11"].pack_forget()
    buttons["2"].pack_forget()
    buttons["22"].pack_forget()
    buttons["3"].pack_forget()
    buttons["33"].pack_forget()
    buttons["4"].pack_forget()
    buttons["5"].pack(side=tk.BOTTOM,anchor=tk.SE)
def ayarlar():
    settings=tk.Tk()
    settings.config(width=300,height=300)
    settings.attributes("-topmost",True)
    adsoyad=tk.Label(settings,text="Adınız Soyadınız")
    adsoyad.grid(row=0)
    name=tk.Entry(settings)
    name.grid(row=1)
    firmaadi=tk.Label(settings,text="Firma Adınız")
    firmaadi.grid(row=2)
    firma=tk.Entry(settings)
    firma.grid(row=3)
    imhaneden=tk.Label(settings,text="İmha Nedeni?")
    imhaneden.grid(row=4)
    neden=tk.Entry(settings)
    neden.grid(row=5)
    kaydet=tk.Button(settings,text="Kaydet",command="")
    kaydet.grid(row=6)

#pages end
# --- functions ---
sayac=0
def refresh():

    mlb.after(1000,refresh)
    os.system('lsblk /dev/sd? --nodeps --output SERIAL >kontrol.lst')

    if open('kontrol.lst','r').readlines()!=open('serial.lst','r').readlines():
        os.system('lsblk /dev/sd? --nodeps --output NAME >name.lst')
        os.system('lsblk /dev/sd? --nodeps --output MODEL >model.lst')
        os.system('lsblk /dev/sd? --nodeps --output SERIAL >serial.lst')
        os.system('lsblk /dev/sd? --nodeps --output SIZE >size.lst')
        os.system('lsblk /dev/sd? --nodeps --output STATE >state.lst')
        name = open("name.lst","r")
        model = open("model.lst", "r")
        serial = open("serial.lst", "r")
        size = open("size.lst", "r")
        state = open("state.lst", "r")
        name=name.readlines()
        model=model.readlines()
        serial=serial.readlines()
        size=size.readlines()
        state=state.readlines()
        count = 0
        for line in state:
            count = count + 1

        mlb.delete(0, END)
        for x in range(0,count):
            if "running" in state[x]:
                state[x]=state[x].replace('\n','')
                size[x]=size[x].replace('\n','')
                serial[x]=serial[x].replace('\n','')
                model[x]=model[x].replace('\n','')
                name[x]=name[x].replace('\n','')
                mlb.insert(END, ('%s' % name[x], '%s'% model[x], '%s' % serial[x], '%s'% size[x],'%s'% state[x],))



class MultiListbox(Frame):
    def __init__(self, master, lists):
        Frame.__init__(self, master)
        self.lists = []
        for l, w in lists:
            frame = Frame(self);
            frame.pack(side=LEFT, expand=YES, fill=BOTH)
            Label(frame, text=l, borderwidth=1, relief=RAISED).pack(fill=X)
            lb = Listbox(frame, width=w, borderwidth=0, selectborderwidth=0,
                         relief=FLAT, exportselection=FALSE)
            lb.pack(expand=YES, fill=BOTH)
            self.lists.append(lb)
            lb.bind('<B1-Motion>', lambda e, s=self: s._select(e.y))
            lb.bind('<Button-1>', lambda e, s=self: s._select(e.y))
            lb.bind('<Leave>', lambda e: 'break')
            lb.bind('<B2-Motion>', lambda e, s=self: s._b2motion(e.x, e.y))
            lb.bind('<Button-2>', lambda e, s=self: s._button2(e.x, e.y))
        frame = Frame(self);
        frame.pack(side=LEFT, fill=Y)
        Label(frame, borderwidth=1, relief=RAISED).pack(fill=X)
        sb = Scrollbar(frame, orient=VERTICAL, command=self._scroll)
        sb.pack(expand=YES, fill=Y)
        self.lists[0]['yscrollcommand'] = sb.set

    def _select(self, y):
        row = self.lists[0].nearest(y)
        self.selection_clear(0, END)
        self.selection_set(row)
        return 'break'

    def _button2(self, x, y):
        for l in self.lists: l.scan_mark(x, y)
        return 'break'

    def _b2motion(self, x, y):
        for l in self.lists: l.scan_dragto(x, y)
        return 'break'

    def _scroll(self, *args):
        for l in self.lists:
            apply(l.yview, args)

    def curselection(self):
        return self.lists[0].curselection()

    def delete(self, first, last=None):
        for l in self.lists:
            l.delete(first, last)

    def get(self, first, last=None):
        result = []
        for l in self.lists:
            result.append(l.get(first, last))
        if last: return apply(map, [None] + result)
        return result

    def index(self, index):
        self.lists[0].index(index)

    def insert(self, index, *elements):
        for e in elements:
            i = 0
            for l in self.lists:
                l.insert(index, e[i])
                i = i + 1

    def size(self):
        return self.lists[0].size()

    def see(self, index):
        for l in self.lists:
            l.see(index)

    def selection_anchor(self, index):
        for l in self.lists:
            l.selection_anchor(index)

    def selection_clear(self, first, last=None):
        for l in self.lists:
            l.selection_clear(first, last)

    def selection_includes(self, index):
        return self.lists[0].selection_includes(index)

    def selection_set(self, first, last=None):
        for l in self.lists:
            l.selection_set(first, last)

def smart_filter():
    with open('s.lst') as file:
        ss=open("smart.lst","w")
        for l in enumerate(file):
           if l[0]>=4:
             satir=str(l[1])
             ss.write(satir)
    ss.close()
    with open('s.lst') as file:
        ss=open("smart.lst","w")
        for l in enumerate(file):
           if l[0]>=4:
               satir=str(l[1])
               ss.write(satir)
        ss.close()
    #ss=open("s-islenmis.lst","w")
    with open("smart.lst") as smart:
        ss=open("s-islenmis.lst","w")
        for l in smart.readlines():
            satir=l.split(':')
            satir[1]=satir[1].strip()
            ss.write(satir[1]+"\n")
        ss.close()

global disk
def disk_id():
    disk=getir()
    if disk is not None:
        value=mlb.get(disk)
        info.config(text=value)
        return disk
    else:
        return None
def smart_info():
    info.after(100,smart_info)
    id=disk_id()
    if id is not None:
        if id==0:
            os.system("smartctl -i /dev/sda >s.lst")
            smart_filter()
        elif id==1:
            os.system("smartctl -i /dev/sdb >s.lst")
            smart_filter()
        elif id==2:
            os.system("smartctl -i /dev/sdc >s.lst")
            smart_filter()
        elif id==3:
            os.system("smartctl -i /dev/sdd >s.lst")
            smart_filter()
        elif id==4:
            os.system("smartctl -i /dev/sdf >s.lst")
            smart_filter()
        elif id==5:
            os.system("smartctl -i /dev/sdg >s.lst")
            smart_filter()
        elif id==6:
            os.system("smartctl -i /dev/sdh >s.lst")
            smart_filter()
        elif id==7:
            os.system("smartctl -i /dev/sdi >s.lst")
            smart_filter()



def getir():
    if mlb.curselection():
        index=str(mlb.curselection())
        index=index.replace('(' ,'')
        index=index.replace(',)','')
        index=int(index)
        return index
    else:
        return None
# --- main ---

root = tk.Tk()
root.config(width=600,height=600)
footer=Frame(root)
header=Frame(root)
#root.attributes('-fullscreen',True)
# lisans=tk.Entry(root)#lisans girdisi
func = {  # sayfalar için fonksiyon
    "1": page1,
    "2": page2,
    "3": page3,
    "4": page4,
    "ayarlar":ayarlar,
}
buttons = {  # butonlar için fonksiyonlar
    "1": tk.Button(footer, text="Sonraki ", command=func["1"]),
    "11": tk.Button(footer, text="Önceki", command=func["1"]),
    "2": tk.Button(footer, text="Sonraki", command=func["2"]),
    "22": tk.Button(footer, text="Önceki", command=func["2"]),
    "3": tk.Button(footer, text="Sonraki ", command=func["3"]),
    "33": tk.Button(footer, text="Önceki", command=func["3"]),
    "4": tk.Button(footer, text="Sonraki ", command=func["4"]),
    "5": tk.Button(footer, text="Çıkış", command=quit),
    "ayarlar":tk.Button(header,text="Ayarlar",command=ayarlar)
}
labels = {
    "başlık": tk.Label(header, text="WIPE", font=("Arial Bold", 50)),
    "2": tk.Label(root, text="Disk Seçin ve imha edin"),
    "3": tk.Label(root, text="Yöntem seçin"),
    "4": tk.Label(root, text="İşlem Tamam"),


}
os.system("echo ''>serial.lst")
screen_width=root.winfo_screenwidth()
def genislik():
    if screen_width>1300:
        genislik=screen_width*50/100
    elif screen_width<1301:
        genislik=screen_width*60/100
    return genislik

header.config(height=30)
header.config(width=screen_width)
buttons["ayarlar"].pack(side=RIGHT,anchor=tk.NW)
anasol=Frame(root)
anasol.config(width=genislik())
anasag=Frame(root)
anasag.config(width=screen_width-genislik())
info=Label(anasag)
labels["başlık"].pack(expand=YES,fill=BOTH)
mlb = MultiListbox(anasol, (('Bağlantı Noktası', 15), ('Cihaz Adı', 50), ('Seri Numarası', 20), ('Boyut', 10), ('Durum', 20)))
buttons["2"].pack()
header.pack(side=TOP)
footer.pack(side=BOTTOM)
root.mainloop()



