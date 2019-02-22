from tkinter import *


loli = Tk()
janela = int()
loli.geometry("400x200")
def janela1():
    janela = 2
    shota.destroy()
    puss.destroy()
    shot.grid(row=1, column=1)
    pussy.grid(row=3, column=1)
def janela2():
    janela = 1
    shot.destroy()
    pussy.destroy()
    shota = Label(loli, text="kkki")
    puss = Button(loli, text="aaa", command=janela1)
    shota.grid(row=1, column=1)
    puss.grid(row=3, column=1)


shota = Label(loli, text="kkki")
puss = Button(loli, text="aaa", command=janela1)
shota.grid(row=1, column=1)
puss.grid(row=3, column=1)
shot = Label(loli, text="Touch me, Senpai")
pussy = Button(loli, text="Click here to go to jail", command=janela2)






loli.mainloop()