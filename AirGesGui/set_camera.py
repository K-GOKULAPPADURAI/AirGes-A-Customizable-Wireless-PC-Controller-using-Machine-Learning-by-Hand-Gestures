import tkinter as tk
root1 = tk.Tk()
master=tk.PhotoImage(file= "c:/Users/APPAtacker.py/Desktop/im/hand.ppm"
, master=root1)
root1.title('Set Camera')
sc_frame = tk.Canvas(root1)
def show():

    out.config(text = 'Streaming on '+ clicked.get())
    r=clicked.get()
    print(r)
    file = open('sc.txt','w')
    file.write(r[-1])
    file.close()
def show1():
    out.config(text='Streaming on '+sclabel2.get("1.0",tk.END))
    file = open('sc.txt','w')
    file.write(str(sclabel2.get("1.0",tk.END)))
    file.close()

    
options = [
	"Camera 0",
	"Camera 1",
	"Camera 2",
	"Camera 3",]
clicked = tk.StringVar()
drop = tk.OptionMenu(sc_frame , clicked ,*options)
clicked.set("Camera 0")
drop.config(padx=20,fg='BlaCk',font='forte 18 bold',bg='wHite')
drop['menu'].config(fg='BlaCk',font='forte 18 bold',bg='wHite')
drop.place(x=500,y=50)
sclabel1=tk.Label(sc_frame,text="Link",padx=20,fg='BlaCk',font='forte 20 bold',bg='wHite')
sclabel1.place(x=150, y=240)
sclabel2=tk.Text(sc_frame,height = 1, width = 32,font='timesnewroman 19 bold')
sclabel2.place(x=250, y=240)
button = tk.Button(sc_frame , text = "Stream cam" ,padx=10,fg='BlaCk',font='forte 18 bold',
                   bg='wHite' ,command=show).place(x=390,y=150)
button = tk.Button(sc_frame , text = "Stream link" ,padx=10,fg='BlaCk',font='forte 18 bold',
                   bg='wHite' ,command=show1).place(x=390,y=320)

sclabel=tk.Label(sc_frame,text="Select Camera",padx=20,fg='BlaCk',font='forte 20 bold',bg='wHite')
sclabel.place(x=150, y=50)
out=tk.Label(sc_frame,text='',padx=20,fg='BlaCk',font='forte 20 bold',bg='wHite')
out.place(x=50,y=500)
sc_frame.create_image(500,400,image = master)
sc_frame.pack(fill='both', expand=True)
root1.geometry('900x550')
root1.resizable(0,0)
root1.mainloop()
