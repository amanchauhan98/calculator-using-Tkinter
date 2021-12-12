from tkinter import *
from tkinter import font
root = Tk()
root.title("Calculator")
root.geometry("300x500")
def click(event):
    global scvalue
    text = event.widget.cget("text")
    
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else :
            try :
                value = eval(screen.get())
            except Exception as e:
                value = "ERROR"    

        scvalue.set(value)
        screen.update()    

    elif text == "C":
        scvalue.set("")
        screen.update()
    else :
        scvalue.set(scvalue.get() + text)
        screen.update()

 

scvalue = StringVar()
scvalue.set("")
screen = Entry(root,width=2 ,font="lucida 20 bold", textvariable=scvalue, relief=SUNKEN)
screen.pack(fill=X)

f = Frame(root, bg="grey")
b = Button(f, text= "9", padx=10, pady=10,font="lucida 8 bold", fg="red",bg="yellow")
b.pack(side=LEFT, padx=10,pady=10)
b.bind("<Button-1>", click)
b = Button(f, text= "8", padx=10, pady=10,font="lucida 8 bold",fg="red",bg="yellow")
b.pack(side=LEFT, padx=10,pady=10)
b.bind("<Button-1>", click)
b = Button(f, text= "7", padx=10, pady=10,font="lucida 8 bold", fg="red",bg="yellow")
b.pack(side=LEFT, padx=10,pady=10)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text= "6", padx=10, pady=10,font="lucida 8 bold", fg="red",bg="yellow")
b.pack(side=LEFT, padx=10,pady=10)
b.bind("<Button-1>", click)
b = Button(f, text= "5", padx=10, pady=10,font="lucida 8 bold", fg="red",bg="yellow")
b.pack(side=LEFT, padx=10,pady=10)
b.bind("<Button-1>", click)
b = Button(f, text= "4", padx=10, pady=10,font="lucida 8 bold", fg="red",bg="yellow")
b.pack(side=LEFT, padx=10,pady=10)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text= "3", padx=10, pady=10,font="lucida 8 bold", fg="red",bg="yellow")
b.pack(side=LEFT, padx=10,pady=10)
b.bind("<Button-1>", click)
b = Button(f, text= "2", padx=10, pady=10,font="lucida 8 bold", fg="red",bg="yellow")
b.pack(side=LEFT, padx=10,pady=10)
b.bind("<Button-1>", click)
b = Button(f, text= "1", padx=10, pady=10,font="lucida 8 bold", fg="red",bg="yellow")
b.pack(side=LEFT, padx=10,pady=10)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text= "0", padx=10, pady=10,font="lucida 8 bold", fg="red",bg="yellow")
b.pack(side=LEFT, padx=10,pady=10)
b.bind("<Button-1>", click)
b = Button(f, text= "00", padx=10, pady=10,font="lucida 8 bold", fg="red",bg="yellow")
b.pack(side=LEFT, padx=10,pady=10)
b.bind("<Button-1>", click)
b = Button(f, text= "=", padx=10, pady=10,font="lucida 8 bold", fg="red",bg="yellow")
b.pack(side=LEFT, padx=10,pady=10)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text= "+", padx=10, pady=10,font="lucida 8 bold", fg="red",bg="yellow")
b.pack(side=LEFT, padx=10,pady=10)
b.bind("<Button-1>", click)
b = Button(f, text= "-", padx=10, pady=10,font="lucida 8 bold", fg="red",bg="yellow")
b.pack(side=LEFT, padx=10,pady=10)
b.bind("<Button-1>", click)
b = Button(f, text= "*", padx=10, pady=10,font="lucida 8 bold",fg="red",bg="yellow")
b.pack(side=LEFT, padx=10,pady=10)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text= "/", padx=10, pady=10,font="lucida 8 bold",fg="red",bg="yellow")
b.pack(side=LEFT, padx=10,pady=10)
b.bind("<Button-1>", click)
b = Button(f, text= "%", padx=10, pady=10,font="lucida 8 bold",fg="red",bg="yellow")
b.pack(side=LEFT, padx=10,pady=10)
b.bind("<Button-1>", click)
b = Button(f, text= "C", padx=10, pady=10,font="lucida 8 bold",bg="red")
b.pack(side=LEFT, padx=10,pady=10)
b.bind("<Button-1>", click)
f.pack()

root.mainloop()