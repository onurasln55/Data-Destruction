from tkinter import *
from tkinter import messagebox

root = Tk()

def page3():
    list = Listbox(root)
    list.insert(END, "disk")
    list.pack()
    buttons["check"].pack_forget()
    license.pack_forget()
def check(a):
    print("check ediliyor")
    if license.get() != "":
        if license.get() == "a":
            checked()
        else:
            unchecked()
    else:
        unchecked()
    return 1

func = {  # sayfalar için fonksiyon
    #"check":lambda check(license),
    "3": page3,
}
buttons = {  # butonlar için fonksiyonlar
    "check": Button(root, text="check ", command=lambda :check(license)),

}

license = Entry(root)
license.pack()
buttons["check"].pack()
licensedogru = Label()

def checked():
    messagebox.showinfo("license", "lisans Doğrulandı")
    page3()
def unchecked():
    messagebox.showwarning("license", "lisans Doğrulanamadı...")


root.mainloop()
