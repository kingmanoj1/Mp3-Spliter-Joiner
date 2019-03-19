from tkinter import *

r=Tk()
def join():
        
    r=Tk()

    
    l=[]
    def slct(): 
        
        fname=askopenfilename()
        lst.insert(END,fname)
        l.append(fname)    

    def jon():
        n=e.get()
        f1=open(n,"ab")
        for i in l:       
            f2=open(i,"rb")
            print(i)
            data=f2.read()        
            f1.write(data)
            f2.close()
        f1.close()
        showinfo("Message","Song Joined")

            
    def inpt():
        dfile=asksaveasfilename()
        e.insert(0,str(dfile))

    r.geometry('800x600+50+50')
    r.resizable(0,0)
    r.title("Mp3 Joiner")
    lst=Listbox(r,font=('arial',15))
    b1=Button(r,text='browse',font=('arial',15),command=slct)
    b2=Button(r,text='browse',font=('arial',15),command=inpt)
    b3=Button(r,text='Join',font=('arial',15),command=jon)

    lbl=Label(r,text="Destination",font=('arial',15))
    lbl2=Label(r,text="Mp3 Joiner",font=("arial",30))
    lbl3=Label(r,text="Choose Your Song",font=("arial",15))

    e=Entry(r,font=('arial',15))

    lbl.place(x=138,y=385)
    lbl2.place(x=270,y=25)
    lbl3.place(x=75,y=100)

    lst.place(x=250,y=100)

    b2.place(x=485,y=380)
    b1.place(x=485,y=100)
    b3.place(x=250,y=427)

    e.place(x=250,y=385)

    r.mainloop()
 #------------------------------------------------------------


def split():

    r=Tk()
    def opn():
        fname=askopenfilename()
        e1.insert(0,str(fname))

    def split():
        fname=e1.get()
        part=e2.get()
        part=int(part)
        fn=len(fname)
        fn2=fn-4
        if os.path.exists(fname):
            total=int(os.path.getsize(fname))
            num=total/part
            i=1
            while i<=part:
                a=int(num*i-num)
                b=int(num*i)
                f=open(fname,"rb")
                data=f.read(int(total))
                z=data[a:b]
                nm=fname[0:fn2:1]+"_split_"+str(i)+".mp3"
                f2=open(nm,"wb")
                f2.write(z)            
                i+=1
                f2.close()
                f.close()
        showinfo('Message',"Song Splited")

            



    r.geometry('800x400+50+50')
    r.title('Song Spliter')
    r.resizable(0,0)
    fnt=('vardana',19)
    l1=Label(r,text='Choose file',font=fnt)
    l2=Label(r,text='Mp3 Spliter',font=('vardana',30),bg='blue',fg='white')
    l3=Label(r,text="Number of Partition",font=fnt)

    e1=Entry(r,font=fnt)
    e2=Entry(r,font=fnt)


    b1=Button(r,text="Browse",font=fnt,command=opn)
    b2=Button(r,text="Split",font=fnt,fg='white',bg='green',activebackground='white',command=split)

    b1.place(x=550,y=95)
    b2.place(x=299,y=240)
    e1.place(x=250,y=100)
    e2.place(x=340,y=180)
    l2.place(x=240,y=20)
    l1.place(x=100,y=100)
    l3.place(x=100,y=180)

    r.mainloop()

r.geometry('400x400+420+80')
r.resizable(0,0)
b1=Button(r,text="Join",command=join,font=("arial",25))
b2=Button(r,text="Split",command=split,font=("arial",25))

b1.place(x=170,y=100)
b2.place(x=170,y=170)

r.mainloop()