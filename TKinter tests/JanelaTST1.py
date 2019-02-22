from tkinter import *

loli = Tk()

shota = Label(loli, text="Touch me, Senpai")
shota.grid(row=1, column=2)


def youtouchedme():
    shota = Label(loli, text="You're going to jail")
    shota.grid(row=1, column=2)


pussy = Button(loli, text="Click here to go to jail", command=youtouchedme)
pussy.grid(row=5, column=1)

butt = Button(loli, text="click here to scape", fg="blue", command=loli.destroy)
butt.grid(row=6, column=3
          )

loli.geometry("400x200")
loli.mainloop()