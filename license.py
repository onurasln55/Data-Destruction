from tkinter import *
from tkinter import messagebox
root = Tk()#main window
def page3():#next page
    list = Listbox(root)
    list.insert(END, "disk")
    list.pack()
    buttons["check"].pack_forget()
    license.pack_forget()
def check(a):#license check
    print("check ediliyor")
    if license.get() != "":
        if license.get() == "a":
            checked()
        else:
            unchecked()
    else:
        unchecked()
    return 1
func = {  # func listed
    #"check":lambda check(license),
    "3": page3,
}
buttons = {  # buttons list
    "check": Button(root, text="check ", command=lambda :check(license)),
}
license = Entry(root)#license entry
license.pack()
buttons["check"].pack()
licensedogru = Label()
def checked():
    messagebox.showinfo("license", "lisans Doğrulandı")
    page3()#href page
def unchecked():
    messagebox.showwarning("license", "lisans Doğrulanamadı...")
    license.delete(0 , END)# entry free
root.mainloop()
