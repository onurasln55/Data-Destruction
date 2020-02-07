import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import os
import datetime

#import apply as apply
silme_modlari={
"Zeroes":"",
"Random Random Zero (6 passes)":"",
"NATO Standard (7 passes)":"",
"Pseudo-Random":"",
"Pseudo-Random & Zeroes (2 passes)":"",
}
##pages start
def anasayfa():
    labels["2"].pack_forget()
    labels["3"].pack_forget()
    labels["4"].pack_forget()
    labels["silinecek"].pack_forget()
    labels["silme_yontemi"].pack_forget()
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
    secim.pack_forget()
    buttons["seç"].pack_forget()
def disk_secim():
    labels["2"].pack()
    labels["3"].pack_forget()
    labels["4"].pack_forget()
    labels["silinecek"].pack_forget()
    labels["silme_yontemi"].pack_forget()
    secim.pack_forget()
    anasol.pack(side=LEFT)
    anasag.pack(side=RIGHT)
    info.pack()
    mlb.pack(expand=YES, fill=BOTH,ipady=(100),side=RIGHT)

    buttons["1"].pack_forget()
    buttons["11"].pack()
    buttons["2"].pack_forget()
    buttons["22"].pack_forget()
    buttons["3"].pack()
    buttons["33"].pack_forget()
    buttons["4"].pack_forget()
    buttons["seç"].pack_forget()
    refresh()
    smart_info()

def yontem_sec():
    labels["2"].pack_forget()
    labels["3"].pack()
    labels["4"].pack_forget()
    labels["silinecek"].pack()
    labels["silme_yontemi"].pack()
    secim.pack()
    buttons["seç"].pack()
    mlb.pack_forget()
    info.pack_forget()
    anasol.pack_forget()
    anasag.pack_forget()
    buttons["1"].pack_forget()
    buttons["11"].pack_forget()
    buttons["2"].pack_forget()
    buttons["22"].pack(side=tk.BOTTOM,anchor=tk.SE)
    buttons["3"].pack_forget()
    buttons["33"].pack_forget()

    buttons["4"].pack(side=tk.BOTTOM,anchor=tk.SE)

def imha_ve_rapor():
    labels["2"].pack_forget()
    labels["3"].pack_forget()
    labels["silinecek"].pack_forget()
    labels["silme_yontemi"].pack_forget()
    labels["4"].pack()
    secim.pack_forget()
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
    buttons["seç"].pack_forget()
    buttons["5"].pack(side=tk.BOTTOM,anchor=tk.SE)

def ayarlar():
    mainsettings.pack()
    label=Label(mainsettings, text="Görevli Kişi",font=10)
    label.grid(row=0,sticky="W")
    entry1.grid(row=0, column=1)
    label=Label(mainsettings, text="Görevlendiren Firma", font=10)
    label.grid(row=1)
    entry2.grid(row=1, column=1)
    button1=Button(mainsettings, text="Kaydet",command=kaydet)
    button1.grid(row=2, column=1)
def kaydet():
    raporcu=entry1.get()
    firma=entry2.get()
    with open("imhaci.lst",'w') as test:
        sonuc=test.write(raporcu+","+firma)
        if sonuc:
            tk.messagebox.showinfo(title="Başarılı",message="Kaydedilmiştir.")
            mainsettings.pack_forget()
def ok():
    print ("Yöntem:" + variable.get())
    disk=getir()
    value=mlb.get(disk)
    print("Disk:%s"%value[0])
    print("Seri Numarası:%s"%value[2])
    print("Boyut:%s"%value[3])
    with open("rapor.txt",'w') as file:
        tarihsaat = datetime.datetime.now().strftime("%d-%m-%Y %H:%M");
        file.close()
        rapor=open("rapor.txt",'a')
        rapor.write("İşlem Başlangıç Zamanı:")
        rapor.write(tarihsaat)
        rapor.write("\n")
        os.system("shred -vz -n 0 /dev/%s"%value[0])
        tarihsaat = datetime.datetime.now().strftime("%d-%m-%Y %H:%M");
        rapor.write("İşlem Bitiş Zamanı:")
        rapor.write(tarihsaat)
        yazar=open("imhaci.lst",'r')
        yazarbilgileri=yazar.readline()
        parcali=yazarbilgileri.split(',')
        yazar.close()
        yazar=parcali[0]
        firma=parcali[1]
        rapor.write("\n")
        rapor.write("Görevli kişi:")
        rapor.write(yazar)
        rapor.write("\n")
        rapor.write("Firma:")
        rapor.write(firma)
        rapor.write("\n")
        rapor.write("Silme Metodu:")
        rapor.write("")

        rapor.close()
        tk.messagebox.showinfo('İşlem Bitti','İşlem tamamlanmıştır iyi günler dileriz.')
def imha_et():
    MsgBox = tk.messagebox.askquestion ('Emin misiniz?','Doğru diski seçtiğinizden eminseniz evet e tıklayınız.(Yapılan işlemden sonra geri dönüş olmayacaktır)',icon = 'warning')
    if MsgBox == 'yes':
        tk.messagebox.showinfo('Uyarı','Yapılan işlem süresince bilgisayarı kapatmayın.İmha edilen diski sistemden çıkartmayın. İşlem bitince ekranda uyarı mesajı olacaktır.')
        ok()



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
    with open('s.lst')as usb:
        for i in usb.readlines():
            if i.lower().find("unknown usb bridge")!=-1:
                print(i)

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

def it_is_smart():
    sayac=0
    with open('s.lst')as usb:
        for i in usb.readlines():
            if i.lower().find("unknown usb bridge")!=-1:
                sayac=sayac+1
    if sayac>0:
        ss=open("smart.lst","w")
        ss.write("Cihazda smart özelliği bulunmamaktadır.")
    else:
        smart_filter()

def disk_id():
    disk=getir()
    if disk is not None:
        value=mlb.get(disk)
        with open("smart.lst") as file:
            smartyazisi=file.read()
        info.config(text=smartyazisi)
        return disk
    else:
        return None
def smart_info():
    info.after(100,smart_info)
    id=disk_id()
    if id is not None:
        if id==0:
            os.system("smartctl -i /dev/sda >s.lst")
        elif id==1:
            os.system("smartctl -i /dev/sdb >s.lst")
        elif id==2:
            os.system("smartctl -i /dev/sdc >s.lst")
        elif id==3:
            os.system("smartctl -i /dev/sdd >s.lst")
        elif id==4:
            os.system("smartctl -i /dev/sdf >s.lst")
        elif id==5:
            os.system("smartctl -i /dev/sdg >s.lst")
        elif id==6:
            os.system("smartctl -i /dev/sdh >s.lst")
        elif id==7:
            os.system("smartctl -i /dev/sdi >s.lst")
        it_is_smart()

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

root.title("PROWIPE")
footer=Frame(root)
header=Frame(root)
bilgi=Frame(root)
root.attributes('-fullscreen',True)
name=StringVar()
lastname=StringVar()
mainsettings=Frame(root)
entry1 = Entry(mainsettings,textvariable=name)
entry2 = Entry(mainsettings,textvariable=lastname)
# lisans=tk.Entry(root)#lisans girdisi
func = {  # sayfalar için fonksiyon
    "1": anasayfa,
    "2": disk_secim,
    "3": yontem_sec,
    "4": imha_ve_rapor,
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
    "seç":tk.Button(root, text="Seç", command=imha_et)
}
labels = {
    "başlık": tk.Label(header, text="PROWIPE", font=("Arial Bold", 50)),
    "2": tk.Label(root, text="Disk Seçin ve imha edin"),
    "3": tk.Label(root, text="Yöntem seçin"),
    "4": tk.Label(root, text="İşlem Tamam"),
    "silinecek":tk.Label(bilgi),
    "silme_yontemi":tk.Label(root,text="Silme yöntemini seçiniz")
}
yontemler = [
"Zeroes",
"Random Random Zero (6 passes)",
"NATO Standard (7 passes)",
"Pseudo-Random",
"Pseudo-Random & Zeroes (2 passes)"
]
variable = StringVar(root)
variable.set(yontemler[0])
secim = OptionMenu(root, variable, *yontemler)
secim.config(width=40)

os.system("echo ''>serial.lst")
screen_width=root.winfo_screenwidth()
def genislik():
    if screen_width>1300:
        genislik=screen_width*30/100
    elif screen_width<1301:
        genislik=screen_width*30/100
    return genislik
menubar = Menu(root)
menubar.add_command(label="Ayarlar", command=func["ayarlar"])
menubar.add_command(label="Çıkış", command=root.quit)
header.config(height=30)
header.config(width=screen_width)
root.config(menu=menubar)
anasol=Frame(root)
anasol.config(width=genislik())
anasag=Frame(root)
anasag.config(width=screen_width-genislik())
info=Label(anasag)
labels["başlık"].pack(expand=YES,fill=BOTH)
mlb = MultiListbox(anasol, (('Bağlantı Noktası', 15), ('Cihaz Adı', 25), ('Seri Numarası', 25), ('Boyut', 10)))
buttons["2"].pack()
header.pack(side=TOP)
footer.pack(side=BOTTOM)
root.mainloop()


