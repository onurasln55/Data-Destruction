from tkinter import *
import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import messagebox
import os
import datetime
root=Tk()

def ayarlar():
    ayar_penceresi=Toplevel(root)
    ayar_penceresi.geometry("500x250")
    ayar1=Frame(ayar_penceresi)
    label={
        "m_bilgileri":tk.Label(ayar1,text="Müşteri Bilgileri"),
        "m_isim":tk.Label(ayar1,text="İsim"),
        "m_adres":tk.Label(ayar1,text="Adres"),
        "c_bilgileri":tk.Label(ayar1,text="Cihaz Sahibi Bilgileri"),
        "c_sahip":tk.Label(ayar1,text="İsim"),
        "gtp_bilgileri":tk.Label(ayar1,text="Görevli Teknik Personel Bilgileri"),
        "gtp_isim":tk.Label(ayar1,text="İsim"),
        "gtp_firma":tk.Label(ayar1,text="Firma"),
        "io_bilgisi":tk.Label(ayar1,text="İmha Onayı Veren Kişi"),
        "io_isim":tk.Label(ayar1,text="İsim"),
        "io_firma":tk.Label(ayar1,text="Firma"),
        }
    ######      AYARLAR KİŞİ BİLGİLERİ BAŞLANGIÇ
    m_isim=StringVar()
    m_adres=StringVar()
    c_sahip=StringVar()
    gtp_isim=StringVar()
    gtp_firma=StringVar()
    io_isim=StringVar()
    io_firma=StringVar()

    ####        AYARLAR KİŞİ BİLGİLERİ SON
    entry={
    "m_isim":tk.Entry(ayar1,textvariable=m_isim),
    "m_adres":tk.Entry(ayar1,textvariable=m_adres),
    "c_sahip":tk.Entry(ayar1,textvariable=c_sahip),
    "gtp_isim":tk.Entry(ayar1,textvariable=gtp_isim),
    "gtp_firma":tk.Entry(ayar1,textvariable=gtp_firma),
    "io_isim":tk.Entry(ayar1,textvariable=io_isim),
    "io_firma":tk.Entry(ayar1,textvariable=io_firma),

    }
    ayar1.pack()
    with open("settings.lst",'r') as file:
        entry["m_isim"].insert(0,file.readline().strip())
        entry["m_adres"].insert(0,file.readline().strip())
        entry["c_sahip"].insert(0,file.readline().strip())
        entry["gtp_isim"].insert(0,file.readline().strip())
        entry["gtp_firma"].insert(0,file.readline().strip())
        entry["io_isim"].insert(0,file.readline().strip())
        entry["io_firma"].insert(0,file.readline().strip())

    def save():
        with open("settings.lst",'w') as file:
            o1=file.write("%s\n"%entry["m_isim"].get())
            o2=file.write("%s\n"%entry["m_adres"].get())
            o3=file.write("%s\n"%entry["c_sahip"].get())
            o4=file.write("%s\n"%entry["gtp_isim"].get())
            o5=file.write("%s\n"%entry["gtp_firma"].get())
            o6=file.write("%s\n"%entry["io_isim"].get())
            o7=file.write("%s\n"%entry["io_firma"].get())

            if o1 and o2 and o3 and o4 and o5 and o6 and o7:
                messagebox.showinfo("Kaydedildi", "Girdiler başarılı olarak kayıt edildi")
            else:
                messagebox.showerror("Kaydedilemedi","Kayıt başarısız olmuştur lütfen tekrar deneyin")

    kaydet=Button(ayar1,text="Kaydet",command=save)
    kaydet.grid(row=6,column=0,columnspan=4)
    label["m_bilgileri"].grid(row=0,columnspan=2,sticky="W",padx=5,pady=5)
    label["m_isim"].grid(row=1,column=0,sticky="W",padx=5,pady=5)
    label["m_adres"].grid(row=2,column=0,sticky="W",padx=5,pady=5)
    entry["m_isim"].grid(row=1,column=1,sticky="W",padx=5,pady=5)
    entry["m_adres"].grid(row=2,column=1,sticky="W",padx=5,pady=5)

    label["c_bilgileri"].grid(row=0,column=2,columnspan=2,sticky="W",padx=5,pady=5)
    label["c_sahip"].grid(row=1,column=2,sticky="W",rowspan=2,padx=5,pady=5)
    entry["c_sahip"].grid(row=1,column=3,sticky="W",rowspan=2,padx=5,pady=5)

    label["gtp_bilgileri"].grid(row=3,columnspan=2,sticky="W",padx=5,pady=5)
    label["gtp_isim"].grid(row=4,column=0,sticky="W",padx=5,pady=5)
    label["gtp_firma"].grid(row=5,column=0,sticky="W",padx=5,pady=5)
    entry["gtp_isim"].grid(row=4,column=1,sticky="W",padx=5,pady=5)
    entry["gtp_firma"].grid(row=5,column=1,sticky="W",padx=5,pady=5)

    label["io_bilgisi"].grid(row=3,columnspan=2,column=2,sticky="W",padx=5,pady=5)
    label["io_isim"].grid(row=4,column=2,sticky="W",padx=5,pady=5)
    label["io_firma"].grid(row=5,column=2,sticky="W",padx=5,pady=5)
    entry["io_isim"].grid(row=4,column=3,sticky="W",padx=5,pady=5)
    entry["io_firma"].grid(row=5,column=3,sticky="W",padx=5,pady=5)
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
                mlb.insert(END, ('%s'% name[x],'%s'% model[x], '%s' % serial[x], '%s'% size[x],))
def imha_et():
    disk=getir()
    if disk != None and disk !='' and disk !=' ':
        MsgBox = tk.messagebox.askquestion ('Emin misiniz?','Doğru diski seçtiğinizden eminseniz evet e tıklayınız.(Yapılan işlemden sonra geri dönüş olmayacaktır)',icon = 'warning')
        if MsgBox == 'yes':
            tk.messagebox.showinfo('Uyarı','Yapılan işlem süresince bilgisayarı kapatmayın.İmha edilen diski sistemden çıkartmayın. İşlem bitince ekranda uyarı mesajı olacaktır.')
            pageone.pack_forget()
            pagetwo.pack()
            ok()
    else:
        tk.messagebox.showinfo('Uyarı','Disk seçimi yapmadınız')
number=0
end_value=100
def end_sector(disk):
    os.system("fdisk -l %s >fdisk.lst"%disk)
    with open("fdisk.lst") as file:
        dosya=file.read()
        dosya=dosya.split()
        j=0
        for i in dosya:
            j=j+1
        for i in range(j):
            if dosya[i]=="sektör":
                max_sector=int(dosya[i-1])
        for i in range(j):
            if dosya[i]=="=" and dosya[i-1]==dosya[i+1]:
                sector_size=int(dosya[i+1])
    return max_sector,sector_size
def wipe(disk,sector_no=0):
    w= open(disk, 'wb')
    w.seek(sector_no*512)
    byte_arr = [0]
    binary_format = bytearray(byte_arr)
    for i in range(512):
        w.seek((sector_no*512)+i)
        w.write(binary_format)
    w.close()

def amount(number):
	Progress_Bar["value"]=number
    #yazi["text"]=str(number)+"%"
def main(disk,number):
    disk_bilgisi=end_sector(disk)
    son_sektor=disk_bilgisi[0]
    yuzde_bir=son_sektor/100
    kontrol=yuzde_bir
    for i in range(0,disk_bilgisi[0],512):
        wipe(disk,i)
        if kontrol==i or kontrol<i:
            number=number+1
            kontrol=kontrol+yuzde_bir
        print(str(number)+"%\t"+str(i)+"/"+str(son_sektor)+"\t"+str(kontrol))
        up(number)
    tk.messagebox.showinfo("Güvenli silme işlemi bitmiştir.")
def up(number):
    Progress_Bar.after(500,amount(number))
    Progress_Bar.update()


def upload(deger):
     Progress_Bar.after(1,amount(deger))
     Progress_Bar.update()

def end_sector(disk):
    os.system("fdisk -l %s >fdisk.lst"%disk)
    with open("fdisk.lst") as file:
        dosya=file.read()
        dosya=dosya.split()
        j=0
        for i in dosya:
            j=j+1
        for i in range(j):
            if dosya[i]=="sektör":
                max_sector=int(dosya[i-1])
        for i in range(j):
            if dosya[i]=="=" and dosya[i-1]==dosya[i+1]:
                sector_size=int(dosya[i+1])
    return max_sector,sector_size

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
        #s.main("/dev/%s"%value[0])
        cihaz="/dev/"+value[0]
        main(cihaz,number)
        #os.system("shred -vz -n 0 /dev/%s"%value[0])
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
def disk_id():
    disk=getir()
    if disk is not None:
        with open("smart.lst") as file:
            smartyazisi=file.read()
        info.config(text=smartyazisi)
        return disk
    else:
        with open("default_smart.lst") as file:
            smartyazisi=file.read()
        info.config(text=smartyazisi)
        return None
def getir():
    if mlb.curselection():
        index=str(mlb.curselection())
        index=index.replace('(' ,'')
        index=index.replace(',)','')
        index=int(index)
        return index
    else:
        return None
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

#sayfalar
pageone=Frame(root)
pagetwo=Frame(root)
header=Frame(pageone)
disklistesi_penceresi=Frame(pageone)
smartozellik_penceresi=Frame(pageone)

silme_penceresi=Frame(pageone)
progressbar_penceresi=Frame(pageone)
footer=Frame(pageone)

header.grid(row=0,columnspan=2)
disklistesi_penceresi.grid(row=1,column=0,padx=15)
smartozellik_penceresi.grid(row=1,column=1)

silme_penceresi.grid(row=2,column=0,pady=30)
progressbar_penceresi.grid(row=3)
footer.grid(row=4)
Progress_Bar=Progressbar(pagetwo,orient="horizontal",length=1000)
Progress_Bar.pack(side="top")
Progress_Bar["value"]=number
Progress_Bar["maximum"]=end_value
def main(disk,number):
    disk_bilgisi=end_sector(disk)
    son_sektor=disk_bilgisi[0]
    yuzde_bir=son_sektor/100
    kontrol=yuzde_bir
    for i in range(0,disk_bilgisi[0],512):
        wipe(disk,i)
        if kontrol==i or kontrol<i:
            number=number+1
            kontrol=kontrol+yuzde_bir
        print(str(number)+"%\t"+str(i)+"/"+str(son_sektor)+"\t"+str(kontrol))
        up(number)
    tk.messagebox.showinfo("Güvenli silme işlemi bitmiştir.")
def up(number):
    Progress_Bar.after(500,amount(number))
    Progress_Bar.update()

buttons = {  # butonlar için fonksiyonlar
    "seç":tk.Button(silme_penceresi, text="Güvenli sil", command=imha_et,state = DISABLED),
}

labels = {
    "başlık": tk.Label(header, text="PROWIPE", font=("Verdana", 30),bg="#F0F8FF"),
    "silme_yontemi":tk.Label(silme_penceresi,text="Silme yöntemini seçiniz"),
    "Disk_Bilgileri":tk.Label(smartozellik_penceresi,text="Disk Bilgileri"),
    "t_baslik":tk.Label(disklistesi_penceresi,text="Disk Listesi")
}
yontemler = [
"Zeroes Metodu",
"Gutmann Metodu",
"NATO Standard Metodu",
"US Army AR 380-19 Metodu",
"DoD 5200.28M",
]

variable = StringVar(silme_penceresi)
variable.set("Silme yöntemini seçiniz!")
secim = OptionMenu(silme_penceresi, variable, *yontemler)
def secim_kontrol():
    secim.after(100,secim_kontrol)
    if variable.get()=="Silme yöntemini seçiniz!":
        buttons["seç"].config(state = DISABLED)
    else:
        buttons["seç"].config(state = NORMAL)
secim_kontrol()
secim.config(width=35)

os.system("echo ''>serial.lst")
ekran_uzunluk=root.winfo_screenwidth()
ekran_yukseklik=root.winfo_screenmmheight()

menubar = Menu(root)
menubar.add_command(label="Ayarlar", command=ayarlar)
menubar.add_command(label="Çıkış", command=root.quit)
root.config(menu=menubar)
labels["t_baslik"].pack()
info=Label(smartozellik_penceresi)
labels["başlık"].pack(expand=YES,fill=BOTH,side=LEFT)
mlb = MultiListbox(disklistesi_penceresi, ( ('bağlantı noktası',0),('Cihaz Adı', 20), ('Seri Numarası', 25), ('Boyut', 10)))
secim.pack(fill=BOTH,expand=YES)

def secim_varsa(secim):
    secim.after(100,secim_varsa)

buttons["seç"].pack(padx=(0),pady=(10),fill=BOTH,expand=YES)
labels["Disk_Bilgileri"].grid(row=0,column=0)
info.grid(row=1,column=0)

mlb.pack(expand=YES, fill=BOTH,ipady=(50),side=RIGHT)
refresh()
smart_info()
pageone.pack()

root.mainloop()
