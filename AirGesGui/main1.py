import tkinter as tk
root = tk.Tk()
master=tk.PhotoImage(file = "c:/Users/APPAtacker.py/Desktop/im/hand.ppm")
big_frame = tk.Canvas(root)
big_frame.pack(expand=True ,fill='both')
big_frame.create_image( 0, 0, image = master, 
                     anchor = "nw")

root.title("AirGes - An Operating system Controller")

Label1 = tk.Label(big_frame, text="AirGes - An Operating system Controller",padx=20,fg='BlaCk',font='forte 30 bold',bg='wHite')
Label1.pack()

label = tk.Label(big_frame,padx=0,pady=20)
label.pack()
path= "c:/Users/APPAtacker.py/Desktop/im/hand.ppm"
def set_camera():
    top = tk.Toplevel()
    master=tk.PhotoImage(file=path,master=top)
    top.title('Set Camera')
    sc_frame = tk.Canvas(top)
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
    top.geometry('900x550')
    top.resizable(0,0)
    top.mainloop()



def app_mode():
    
    top1 = tk.Toplevel()
    master=tk.PhotoImage(file=path, master=top1)
    top1.title('Application Mode')
    app_frame = tk.Canvas(top1)
    app_frame.pack(fill='both', expand=True)
    app_frame.create_image(500,400,image = master)
    sclabel=tk.Label(app_frame,text="Select Application",padx=20,fg='BlaCk',font='forte 20 bold',bg='wHite')
    sclabel.place(x=100, y=50)
    options = [ "Microsoft Power Point", "Microsoft Word","Microsoft Excel","VLC Media Player","Chrome","Groove Music"]
    clicked = tk.StringVar()
    clicked.set("Microsoft Power Point")
    drop = tk.OptionMenu(app_frame , clicked ,*options)
    drop.config(padx=20,fg='Black',font='forte 18 bold',bg='white')
    drop['menu'].config(fg='Black',font='forte 18 bold',bg='white')
    drop.place(x=520,y=50)
    def desc():
    
        file=open('{}.txt'.format(clicked.get()),'r')
        l=[]
        for i in file:
            l.append(i.lower().rstrip('\n'))
        file.close()
        ll=[]
        for i in l:
            ll.append(i.split(','))
        sck=[]
        for i in ll:
            sck.append(i[1].split('+'))
        #print(sck)
        lll=[]
        for i in ll:
            lll.append([i[0],i[-1]])
        #print(lll)

        a1=tk.Label(app_frame,text=['Finger_count','[Desc]'],fg='BlaCk',font='timesnewroman 20 bold',
                    bg='wHite')
        a1.place(x=100,y=150)
        t=150
        for i in lll:
            t+=60
            tk.Label(app_frame,text=str(i).center(40),fg='BlaCk',font='timesnewroman 20 ',
                    bg='wHite').place(x=100,y=t)
               
    def sett():
        from trail import present

    button1 = tk.Button(app_frame , text = "Start Presentation" ,padx=10,fg='BlaCk',
                        font='forte 18 bold',bg='wHite',command=sett).place(x=570,y=380)
    button2 = tk.Button(app_frame , text = "Settings" ,padx=10,fg='BlaCk',
                        font='forte 18 bold',bg='wHite',command=desc).place(x=570,y=320)
    
    top1.geometry('900x500')
    top1.resizable(0,0)
    top1.mainloop()

def set_gesture():
    top = tk.Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    l2 = tk.Label(top, text = "This is toplevel window").pack()
def customize_gesture():
    top = tk.Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    l2 = tk.Label(top, text = "This is toplevel window").pack()
def new_gesture():
    top = tk.Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    l2 = tk.Label(top, text = "This is toplevel window").pack()




button = tk.Button(big_frame, text="  Set Camera ",font='forte 20 bold', fg='black', bg='silver', bd=3, relief='solid', padx=1, pady=1,command=set_camera);button.pack()
button1 = tk.Button(big_frame, text="  App Mode ",font='forte 20 bold', fg='black', bg='silver', bd=3, relief='solid', padx=2, pady=1,command=app_mode);button1.pack()
button3 = tk.Button(big_frame, text="Customize Gesture",font='forte 20 bold', fg='black', bg='silver', bd=3, relief='solid', padx=1, pady=1,command=customize_gesture);button3.pack()
button2 = tk.Button(big_frame, text="  Set Gesture ",font='forte 20 bold',fg='black', bg='silver', bd=3, relief='solid', padx=1, pady=1,command=set_gesture);button2.pack()
button4 = tk.Button(big_frame, text="  New Gesture  ",font='forte 20 bold',fg='black', bg='silver', bd=3, relief='solid', padx=1, pady=1,command=new_gesture);button4.pack()
root.resizable(0,0)
root.geometry('900x550')
#root.maxsize(900, 550)
#root.minsize(900, 550)
root.mainloop()
