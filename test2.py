import tkinter
window = tkinter.Tk()
def page1():
    page2text.pack_forget()
    page3text.pack_forget()
    page1text.pack()

def page2():
    page1text.pack_forget()
    page2text.pack()
    page3text.pack_forget()

def page3():
    page1text.pack_forget()
    page2text.pack_forget()
    page3text.pack()
pagelist="123"
i=iter(pagelist)
page="page"
page1btn = tkinter.Button(window, text="Next", command=page+next(i))
page2btn = tkinter.Button(window, text="Exit", command=quit)

page1text = tkinter.Label(window, text="This is page 1")
page2text = tkinter.Label(window, text="This is page 2")
page3text = tkinter.Label(window, text="This is page 3")

page1btn.pack()
page2btn.pack()
page1text.pack()
window.mainloop()
