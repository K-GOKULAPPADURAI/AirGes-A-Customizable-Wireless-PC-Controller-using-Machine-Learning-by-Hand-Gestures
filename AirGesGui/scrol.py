from tkinter import Tk, Listbox, Button, Scrollbar

def get():
    userline=leftside.get('active')
    print(userline) 

def scale():
    global leftside
    thescale=Tk()
    scroll=Scrollbar(thescale)
    scroll.pack(side='right', fill='y')

    leftside = Listbox(thescale, yscrollcommand = scroll.set)
    for line in range(101):
        leftside.insert('end', "Scale "+str(line))

    leftside.pack(side='left', fill='both')
    scroll.config(command=leftside.yview)

    selectbutton=Button(thescale, text="Select", command=get)
    selectbutton.pack()

    thescale.mainloop()

scale()
