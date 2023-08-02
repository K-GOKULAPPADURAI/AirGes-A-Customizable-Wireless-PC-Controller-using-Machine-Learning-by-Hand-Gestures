import keyboard
from tkinter import ttk
import tkinter as tk
root = tk.Tk()
master=tk.PhotoImage(file = "hand.ppm")
big_frame = tk.Canvas(root)
big_frame.pack(expand=True ,fill='both')
big_frame.create_image( 0, 0, image = master, 
                     anchor = "nw")

root.title("AirGes - An Operating system Controller")

Label1 = tk.Label(big_frame, text="AirGes - An Operating system Controller",padx=20,fg='BlaCk',font='forte 30 bold',bg='wHite')
Label1.pack()

label2 = tk.Label(big_frame,padx=0,pady=20)
label2.pack()
path= "hand.ppm"
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
    clicked0 = tk.StringVar()
    clicked0.set("Microsoft Power Point")
    drop = tk.OptionMenu(app_frame , clicked0 ,*options)
    drop.config(padx=20,fg='Black',font='forte 18 bold',bg='white')
    drop['menu'].config(fg='Black',font='forte 18 bold',bg='white')
    drop.place(x=520,y=50)
    t=150
    a0=tk.Label(app_frame,text='',fg='BlaCk',font='timesnewroman 20 bold',
                    bg='wHite')
    #a0.place(x=100,y=t)
    a1=tk.Label(app_frame,text='',fg='BlaCk',font='timesnewroman 20 ',
                    bg='wHite')
    #a1.place(x=100,y=t+60)
    a2=tk.Label(app_frame,text='',fg='BlaCk',font='timesnewroman 20 ',
                    bg='wHite')
    #a2.place(x=100,y=t+120)
    a3=tk.Label(app_frame,text='',fg='BlaCk',font='timesnewroman 20 ',
                    bg='wHite')
    #a3.place(x=100,y=t+180)
    a4=tk.Label(app_frame,text='',fg='BlaCk',font='timesnewroman 20 ',
                    bg='wHite')
    #a4.place(x=100,y=t+240)
    a5=tk.Label(app_frame,text='',fg='BlaCk',font='timesnewroman 20 ',
                    bg='wHite')
    #a5.place(x=100,y=t+300)
    
    def desc():
    
        file=open('{}.txt'.format(clicked0.get()),'r')
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

        a0.config(text=['Finger_count','[Desc]'])
        a0.place(x=100,y=150)
        t=150
##        for i in lll:
##            t+=60
##            tk.Label(app_frame,text=str(i).center(40),fg='BlaCk',font='timesnewroman 20 ',
##                    bg='wHite').place(x=100,y=t)
        a1.config(text=str(lll[0]).center(40))
        a1.place(x=100,y=t+60)
        a2.config(text=str(lll[1]).center(40))
        a2.place(x=100,y=t+120)
        a3.config(text=str(lll[2]).center(40))
        a3.place(x=100,y=t+180)
        a4.config(text=str(lll[3]).center(40))
        a4.place(x=100,y=t+240)
        a5.config(text=str(lll[4]).center(40))
        a5.place(x=100,y=t+300)
        
               
    def sett():
        file = open('sc.txt','r')
        from exe import present
        cam=int(file.read())
        print(clicked0.get())
        present(cam,appMode=clicked0.get(),cg=0)

    button1 = tk.Button(app_frame , text = "Start Presentation" ,padx=10,fg='BlaCk',
                        font='forte 18 bold',bg='wHite',command=sett).place(x=570,y=380)
    button2 = tk.Button(app_frame , text = "Settings" ,padx=10,fg='BlaCk',
                        font='forte 18 bold',bg='wHite',command=desc).place(x=570,y=320)
    
    top1.geometry('900x500')
    top1.resizable(0,0)
    top1.mainloop()

def set_gesture():
    top2 = tk.Toplevel()
    master=tk.PhotoImage(file=path, master=top2)
    top2.title('Set Gesture')
    set_frame = tk.Canvas(top2)
    set_frame.pack(fill='both', expand=True)
    set_frame.create_image(500,400,image = master)
    sglabel=tk.Label(set_frame,text="Set Controls",padx=20,fg='BlaCk',font='forte 20 bold',bg='wHite')
    sglabel.place(x=100, y=50)
    l1=tk.Label(set_frame,text="Choose Finger count",padx=20,fg='BlaCk',font='forte 20 bold',bg='wHite')
    l1.place(x=100, y=130)
    options = [ "1-One", "2-Two","3-Three","4-Four","5-Five","0-Zero"]
    clicked1 = tk.StringVar()
    clicked1.set("1-One")
    drop = tk.OptionMenu(set_frame, clicked1 ,*options)
    drop.config(padx=20,fg='Black',font='forte 18 bold',bg='white')
    drop['menu'].config(fg='Black',font='forte 18 bold',bg='white')
    drop.place(x=100,y=180)
    sl2=tk.Label(set_frame,text="Press Shortcuts",padx=20,fg='BlaCk',font='forte 20 bold',bg='wHite')
    sl2.place(x=500, y=50)
    variable = tk.StringVar(top2)
    variable.set("select below") # default value
    comb=ttk.Combobox(top2,textvariable=variable,values=['0', '1', '2', '3', '4', '5', '6', '7',
        '8', '9','a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'alt', 'altleft', 'altright', 'apps', 'backspace','ctrl', 'ctrlleft', 'ctrlright','del','delete'
        ,'down', 'end', 'enter', 'esc','f1','f10',
        'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
        'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
        'fn','left','num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
        'num7', 'num8', 'num9','pagedown', 'pageup', 'pause', 'pgdn',
        'pgup', 'playpause','prtsc', 'prtscr', 'right',
        'shift', 'shiftleft', 'shiftright', 'space', 'tab',
        'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
        'command', 'option', 'optionleft', 'optionright']
        )
    comb.config(font='timesnewroman 15')
    comb.place(x=500, y=150)
    
    def set_ges():
        file0=open('setgu.txt','a')
        file0.write(clicked1.get()[0]+','+ll3.get()+'\n')
        print(clicked1.get()[0]+','+ll3.get())
        file0.close()
        
    def start_press():
        file1 = open('sc.txt','r')
        from exe import present
        cam=int(file1.read())
        present(cam,appMode=0,cg=1)

        
    butt= tk.Button(set_frame, text="Set Gesture",font='forte 20 bold', fg='black', bg='white', bd=3, relief='solid', padx=1, pady=1,command=set_ges)
    butt.place(x=400,y=300)
    def add():
        s=comb.get()
        tt='+'
        ll3.insert(len(ll3.get())+1,s+tt)    
    buttons = tk.Button(set_frame, text=" Start presentation ",font='forte 20 bold', fg='black', bg='silver', bd=3, relief='solid', padx=1, pady=1,command=start_press)
    buttons.place(x=400,y=400)
    var=tk.StringVar(set_frame)
    ll3=tk.Entry(set_frame,fg='BlaCk',font='timesnewroman 15',bg='wHite')
    ll3.insert(0,'type keys sperated by +')
    ll3.place(x=500, y=100)
    bute = tk.Button(set_frame, text="add",font='forte 15 bold', fg='black', bg='white', bd=3, relief='solid', padx=1, pady=1,command=add)
    bute.place(x=770, y=100)    
    top2.geometry('900x500')
    top2.resizable(0,0)
    top2.mainloop()

def customize_gesture():
    top3 = tk.Toplevel()
    master=tk.PhotoImage(file=path, master=top3)
    top3.title('Cusotmize Gesture')
    cus_frame = tk.Canvas(top3)
    cus_frame.pack(fill='both', expand=True)
    cus_frame.create_image(500,400,image = master)
    cuslabel=tk.Label(cus_frame,text="Change a Gesture",padx=20,fg='BlaCk',font='forte 20 bold',bg='wHite')
    cuslabel.place(x=100, y=50)
    top3.geometry('900x500')
    top3.resizable(0,0)
    top3.mainloop()

def new_gesture():    
    top4 = tk.Toplevel()
    master=tk.PhotoImage(file=path, master=top4)
    top4.title('New Gesture')
    cus_frame = tk.Canvas(top4)
    cus_frame.pack(fill='both', expand=True)
    cus_frame.create_image(500,400,image = master)
    cuslabel=tk.Label(cus_frame,text="Join an Application",padx=20,fg='BlaCk',font='forte 20 bold',bg='wHite')
    cuslabel.place(x=100, y=50)
    top4.geometry('900x500')
    top4.resizable(0,0)
    top4.mainloop()


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
