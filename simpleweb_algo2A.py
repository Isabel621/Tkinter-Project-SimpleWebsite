
#mengimport modul modul yang digunakan
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import *
from PIL import ImageTk,Image

#menentukan ukuran window untuk splash screen
w = Tk()

witdh_of_window = 427
height_of_window = 250
screen_witdh = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_cordinate = (screen_witdh / 2) - (witdh_of_window / 2)
y_cordinate = (screen_height / 2) - (height_of_window / 2)
w.geometry("%dx%d+%d+%d" % (witdh_of_window, height_of_window, x_cordinate, y_cordinate))
w.overrideredirect(1)

#menentukan style untuk progress bar
s= ttk.Style()
s.theme_use('clam')
s.configure('red.Horizontal.TProgressbar', foreground='red', background='#4f4f4f')
progress = Progressbar(w, style='red.Horizontal.TProgressbar', orient=HORIZONTAL, length=500, mode='determinate')

#menentukan ukuran window untuk fitur
#menentukan fitur yang akan ditampilkan
def fitur():
    
    w=Tk()
    w.geometry('900x500')
    w.configure(bg='#262626')
    w.resizable(0,0)
    w.title('Our Website')

    #menentukan frame untuk fitur yang akan ditampilkan
    def default_home():
        f2=Frame(w,width=900,height=455,bg='#262626')
        f2.place(x=0,y=45)
        img4 = PhotoImage(file="home.png")
        l4 = Label(f2, image=img4)
        l4.place(x=-2, y=-2)
        l4.image = img4
        b4=Button(w, width=10, height=1, text='Learn More', command=abtfe, bg='white')
        b4.place(x=425, y=350)
 
    #menentukan frame untuk fitur yang akan ditampilkan
    def abtfe():
        f2=Frame(w,width=900,height=455,bg='#262626')
        f2.place(x=0,y=45)
        img5 = PhotoImage(file="fe.png")
        l5 = Label(f2, image=img5)
        l5.place(x=-2, y=-2)
        l5.image = img5
        b5=Button(w, width=10, height=1, text='Back', command=default_home, bg='white')
        b5.place(x=350, y=430)
        b6 = Button(w, width=10, height=1, text='Next', command=skill, bg='white')
        b6.place(x=490, y=430)
    
    
    #menentukan frame untuk fitur yang akan ditampilkan
    def skill():
        f2=Frame(w,width=900,height=455,bg='white')
        f2.place(x=0,y=45)
        img6 = PhotoImage(file="skill.png")
        l6 = Label(f2, image=img6)
        l6.place(x=-2, y=-2)
        l6.image = img6
        b5=Button(w, width=10, height=1, text='Back', command=abtfe, bg='white')
        b5.place(x=350, y=430)
        b6 = Button(w, width=10, height=1, text='Next', command=karir, bg='white')
        b6.place(x=490, y=430)


    #menentukan frame untuk fitur yang akan ditampilkan
    def karir():
        f2=Frame(w,width=900,height=455,bg='white')
        f2.place(x=0,y=45)
        img7 = PhotoImage(file="karir.png")
        l7 = Label(f2, image=img7)
        l7.place(x=-2, y=-2)
        l7.image = img7
        b5=Button(w, width=10, height=1, text='Back', command=skill, bg='white')
        b5.place(x=350, y=430)
        b6 = Button(w, width=10, height=1, text='Home', command=default_home, bg='white')
        b6.place(x=490, y=430)

    #menentukan frame untuk fitur yang akan ditampilkan
    def ourteam():
        f2=Frame(w,width=900,height=455,bg='#262626')
        f2.place(x=0,y=45)
        img3 = PhotoImage(file="ourteam.png")
        l0 = Label(w, image=img3)
        l0.place(x=0, y=45, relheight=1, relwidth=1)
        l0.image = img3
        b2=Button(w, width=10, height=1, text='Back', command=default_home, bg='white')
        b2.place(x=410, y=430)
       
    
    #menentukan frame untuk fitur yang akan ditampilkan (side bar)
    def toggle_win():
        global f1
        f1=Frame(w,width=200,height=500,bg='#8EA3DC')
        f1.place(x=0,y=0)
        
        #buttons
        def bttn(x,y,text,bcolor,fcolor,cmd):
        
            def on_entera(e):
                myButton1['background'] = bcolor 
                myButton1['foreground']= '#262626' 

            def on_leavea(e):
                myButton1['background'] = fcolor
                myButton1['foreground']= '#262626'

            myButton1 = Button(f1,text=text,
                        width=42,
                        height=2,
                        fg='#262626',
                        border=0,
                        bg=fcolor,
                        activeforeground='#262626',
                        activebackground=bcolor,            
                            command=cmd)
                        
            myButton1.bind("<Enter>", on_entera)
            myButton1.bind("<Leave>", on_leavea)

            myButton1.place(x=x,y=y)

        bttn(-50,80,'MAIN PAGE','#7C90C5','#8EA3DC',default_home)
        bttn(-50,117,'ABOUT  FE','#7C90C5','#8EA3DC',abtfe)
        bttn(-50,154,'SKILL','#7C90C5','#8EA3DC',skill)
        bttn(-50,191,'CAREER','#7C90C5','#8EA3DC',karir)
        bttn(-50,228,'OUR TEAM','#7C90C5','#8EA3DC',ourteam)
        
        #hoverage buttons
        def dele():
            f1.destroy()
            b2=Button(w,image=img1,
                command=toggle_win,
                border=0,
                bg='#262626',
                activebackground='#262626')
            b2.place(x=5,y=8)

        global img2
        img2 = ImageTk.PhotoImage(Image.open("close.png"))

        Button(f1,
            image=img2,
            border=0,
            command=dele,
            bg='#8EA3DC',
            activebackground='#8EA3DC').place(x=5,y=10)
        

    default_home()

    img1 = ImageTk.PhotoImage(Image.open("open.png"))

    global b2
    b2=Button(w,image=img1,
        command=toggle_win,
        border=0,
        bg='#262626',
        activebackground='#262626')
    b2.place(x=5,y=8)

    w.mainloop()

#fungsi untuk menampilkan frame awal (splash screen)
def bar():
    l4=Label(w, text='Loading...', fg='white', bg='#1F44A9')
    lst4=('Calibri (Body)', 10)
    l4.config(font=lst4)
    l4.place(x=0, y=210)

    import time
    r=0
    for i in range(100):
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.01)
        r=r+1
    w.destroy()
    fitur()

progress.place(x=-10, y=235)

#menentukan ukuran frame untuk splash screen
Frame(w, width=427, height=241, bg='#1F44A9').place(x=0, y=0)
b1=Button(w, width=10, height=1, text='Get Started', command=bar, bg='white')
b1.place(x=170, y=150)

#menentukan tulisan yang tampil di splash screen
l1=Label(w, text='Welcome to Our Simple Website', fg='white', bg='#1F44A9')
lst1=('Calibri (Body)', 18, 'bold')
l1.config(font=lst1)
l1.place(x=25, y=80)

w.mainloop()


