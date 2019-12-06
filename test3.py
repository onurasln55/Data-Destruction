import tkinter as tk

# --- functions ---

def page1():
    labels["1"].pack()
    labels["2"].pack_forget()
    labels["3"].pack_forget()

def page2():
    labels["1"].pack_forget()
    labels["2"].pack()
    labels["3"].pack_forget()

def page3():
    labels["1"].pack_forget()
    labels["2"].pack_forget()
    labels["3"].pack()

# --- main ---

window = tk.Tk()

func = {
    "1": page1,
    "2": page2,
    "3": page3,
}


buttons = {
    "1": tk.Button(window, text="Page 1", command=func["1"]),
    "2": tk.Button(window, text="Page 2", command=func["2"]),
    "3": tk.Button(window, text="Page 3", command=func["3"]),
}

labels = {
    "1": tk.Label(window, text="This is page 1"),
    "2": tk.Label(window, text="This is page 2"),
    "3": tk.Label(window, text="This is page 3"),
}    

buttons["1"].pack()
buttons["2"].pack()
buttons["3"].pack()

labels["1"].pack()

window.mainloop()
