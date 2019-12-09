import tkinter as tk
from tkinter.ttk import Combobox

# --- functions ---

def page1():
    buttons["1"].pack_forget()    
    buttons["2"].pack()
    buttons["3"].pack_forget()
    buttons["4"].pack_forget()
    
    labels["1"].pack()
    labels["2"].pack_forget()
    labels["3"].pack_forget()
    labels["4"].pack_forget()

def page2():
    buttons["1"].pack_forget()    
    buttons["2"].pack_forget()
    buttons["3"].pack()
    buttons["4"].pack_forget()

    labels["1"].pack_forget()
    labels["2"].pack()
    labels["3"].pack_forget()
    labels["4"].pack_forget()

    combobox["1"].pack()

def page3():
    buttons["1"].pack_forget()    
    buttons["2"].pack_forget()
    buttons["3"].pack_forget()
    buttons["4"].pack()

    labels["1"].pack_forget()
    labels["2"].pack_forget()
    labels["3"].pack()
    labels["4"].pack_forget()

    
    label= tk.Label(root,text=combobox["1"].get())
    label.pack()
    combobox["1"].pack_forget()

def page4():
    buttons["1"].pack_forget()    
    buttons["2"].pack_forget()
    buttons["3"].pack_forget()
    buttons["4"].pack_forget()
    buttons["5"].pack()

    labels["1"].pack_forget()
    labels["2"].pack_forget()
    labels["3"].pack_forget()
    labels["4"].pack()

    combobox["1"].pack_forget()
# --- main ---

root = tk.Tk()
#root.attributes('-fullscreen',True)

func = {
    "1": page1,
    "2": page2,
    "3": page3,
    "4": page4,
}

buttons = {
    "1": tk.Button(root, text="Next", command=func["1"]),
    "2": tk.Button(root, text="Next", command=func["2"]),
    "3": tk.Button(root, text="Next", command=func["3"]),
    "4": tk.Button(root, text="Next", command=func["4"]),
    "5": tk.Button(root, text="Exit", command=quit),
}

labels = {
    "1": tk.Label(root, text="PROWIPE",font=("Arial Bold",50)),
    "2": tk.Label(root, text="Disk Seçin ve imha edin") ,
    "3": tk.Label(root, text="İmha işlemi sürüyor... "),
    "4": tk.Label(root, text="İşlem Tamam"),
}
combobox={
    "1":Combobox(root,state='readonly'),
}

combobox["1"]["values"]=('Deneme A','Deneme B','Deneme C','Deneme D')

combobox["1"].get()

labels["1"].pack()
buttons["2"].pack()
root.mainloop()
