
from tkinter import *
import tkinter.messagebox
from numpy import *
import pickle

a=1
def dowithdraw(event):
    global y
    global s
    global bal
    for widget in window5.winfo_children():
        widget.destroy()
    f=open('data.txt','r')
    x=f.readlines()
    global p
    for i in x:
        if s in i:
            k=len(i)
            for j in range(k-1,0,-1):
                if(i[j]=='\t'):
                    bal=int(i[(j+1)::])
                    p=j+1
                    print(bal)
                    break
    f.close()
    def subbal(event):

        global bal
        global z
        global y
        depamt=depe1.get()
        print(depamt)
        depamt=int(depamt)
        bal=bal-depamt
        print(bal)
        z=str(bal)
        def updatebal(event):
            global p
            global s
            global z
            global y
            tkinter.messagebox.showinfo("Withdraw","Amount withdrawn successfully...!!!")
            '''f=open('data.txt','r')
            x=f.readlines()
            print(p)
            f.close()
            f=open('data.txt','w')
            for i in x:
                if s in i:
                    f.write("\n")
                    k=len(i)
                    str1=i.replace(y,z)
                    f.write(str1)
                    
                    
            
            f.close()'''
            
        l=Label(window5,text=('Your balance after withdraw --Rs'+z),font=('Arial',16),fg='black',bg='lightblue')
        l.place(x=20,y=130)
        l=Label(window5,text=('PRESS SUBMIT TO withdraw.'),font=('Arial',16),fg='red',bg='lightblue')
        l.place(x=35,y=160)
        sub=Button(window5,text='SUBMIT',bg='red',fg='black',width=6,height=2)
        sub.place(x=100,y=210)
        sub.bind("<Button-1>",updatebal)

        
    
    z=str(bal)
    l=Label(window5,text=('Your current balance is --Rs'+z),font=('Arial',16),fg='black',bg='lightblue')
    l.place(x=20,y=30)
    lab=Label(window5,text=('Amount to:-\ndeposit'),font=('Arial',16),fg='black',bg='lightblue')
    lab.place(x=20,y=60)
    depe1=Entry(window5,width=10,fg='black',bg='white',font=('Arial',16))
    depe1.place(x=130,y=70)
    depe1.bind("<Return>",subbal)

    
def dodeposit(event):
    global y
    
    global s
    global bal
    for widget in window5.winfo_children():
        widget.destroy()
    print('hello')
    f=open('data.txt','r')
    x=f.readlines()
    global p
    for i in x:
        if s in i:
            k=len(i)
            for j in range(k-1,0,-1):
                if(i[j]=='\t'):
                    bal=int(i[(j+1)::])
                    p=j+1
                    print(bal)
                    break
    f.close()
    def addbal(event):
        global bal
        global z
        global y
        depamt=depe1.get()
        print(depamt)
        depamt=int(depamt)
        bal=bal+depamt
        print(bal)
        z=str(bal)
        def updatebal(event):
            global p
            global s
            global z
            global y
            tkinter.messagebox.showinfo("Deposit","Amount deposited successfully...!!!")
            '''f=open('data.txt','r')
            x=f.readlines()
            print(p)
            f.close()
            f=open('data.txt','a')
            for i in x:
                if s in i:
                    f.write("\n")
                    k=len(i)
                    str1=i.replace(y,z)
                    f.write(str1)
                    
                    
            
            f.close()'''
            
        l=Label(window5,text=('Your balance after deposit --Rs'+z),font=('Arial',16),fg='black',bg='lightblue')
        l.place(x=20,y=130)
        l=Label(window5,text=('PRESS SUBMIT TO DEPOSIT.'),font=('Arial',16),fg='red',bg='lightblue')
        l.place(x=35,y=160)
        sub=Button(window5,text='SUBMIT',bg='red',fg='black',width=6,height=2)
        sub.place(x=100,y=210)
        sub.bind("<Button-1>",updatebal)
        exitt=Button(window5,text='EXIT',bg='red',fg='black',width=6,height=2,command=quit)
        exitt.place(x=190,y=210)



    

    z=str(bal)
    l=Label(window5,text=('Your current balance is --Rs'+z),font=('Arial',16),fg='black',bg='lightblue')
    l.place(x=20,y=30)
    lab=Label(window5,text=('Amount to:-\ndeposit'),font=('Arial',16),fg='black',bg='lightblue')
    lab.place(x=20,y=60)
    depe1=Entry(window5,width=10,fg='black',bg='white',font=('Arial',16))
    depe1.place(x=130,y=70)
    depe1.bind("<Return>",addbal)
    
        
        



    
def printprofile(event):
    global loginname
    global s
    print(s)
    for widget in window5.winfo_children():
        widget.destroy()
    
    f=open('data.txt','r')
    x=f.readlines()
    print(x)
    t=0
    for i in x:
        if s in i:
            k=len(i)
            print(k)
            for j in range(k):
                if(i[j]=='\t' and t<=6):
                    t+=1
                if(i[j]=='\t'and t==1):
                    print(j)
                    l=Label(window5,text=('Name:          '+i[0:j]),font=('Arial',16),fg='black',bg='lightblue')
                    l.place(x=20,y=30)
                    n=j+1

                if(i[j]=='\t'and t==2):
                    print(j)
                    l=Label(window5,text=('Email Id:      '+i[n:j]),font=('Arial',16),fg='black',bg='lightblue')
                    l.place(x=20,y=70)
                    n=j+1

                if(i[j]=='\t'and t==3):
                    print(j)
                    l=Label(window5,text=('Contact:       '+i[n:j]),font=('Arial',16),fg='black',bg='lightblue')
                    l.place(x=20,y=110)
                    n=j+1

                if(i[j]=='\t'and t==4):
                    print(j)
                    l=Label(window5,text=('Gender:       '+i[n:j]),font=('Arial',16),fg='black',bg='lightblue')
                    l.place(x=20,y=150)
                    n=j+1

                if(i[j]=='\t'and t==5):
                    print(j)
                    l=Label(window5,text=('Password:    '+i[n:j]),font=('Arial',16),fg='black',bg='lightblue')
                    l.place(x=20,y=190)
                    n=j+1

                if(i[j]=='\t'and t==6):
                    print(j)
                    l=Label(window5,text=('Account No.: '+i[n:j]),font=('Arial',16),fg='black',bg='lightblue')
                    l.place(x=20,y=230)
                    n=j+1

            l=Label(window5,text=('Balance:      '+i[n:k]),font=('Arial',16),fg='black',bg='lightblue')
            l.place(x=20,y=270)
            n=j+1

            
            

                

    f.close()

                    
                
def mainpage(event):

    global a
    if a==1:
        window1.destroy()
        root2.destroy()
    if a==2:
        window3.destroy()
        root3.destroy()

    global root4
    global window4
    global window5
    global accno
    
   
    root4=Tk()
    window4=Frame(root4,width=400,height=50,bg='lightblue')
    root4.title("Account")
    window4.grid(row=0,column=4)
    profilebutton=Button(window4,text='Profile',width=10,height=1,bg='red',fg='white')
    profilebutton.place(x=20,y=20)
    profilebutton.bind("<Button-1>",printprofile)
    
    depositbutton=Button(window4,text='Deposit',width=10,height=1,bg='red',fg='white')
    depositbutton.place(x=150,y=20)
    depositbutton.bind("<Button-1>",dodeposit)

    withdrawbutton=Button(window4,text='Withdraw',width=10,height=1,bg='red',fg='white')
    withdrawbutton.place(x=280,y=20)
    withdrawbutton.bind("<Button-1>",dowithdraw)


    window5=Frame(root4,width=400,height=400,bg='lightblue')
    window5.grid(row=1,column=4)






    
    root4.mainloop()


def filewrite(event):
    global s
    global accno
    lst=[]
    


    accno=int(random.rand()*100000)
    accno=str(accno)
    s=accno
    tkinter.messagebox.showinfo("Account Created","Your account number is:"+accno)

    
    f=open('data.txt','a')
    
    x=namee1.get()                 #Write in file
    lst.append(x)
    lst.append("\t")

    x=emaile2.get()
    lst.append(x)
    lst.append("\t")

    x=phoe3.get()
    lst.append(x)
    lst.append("\t")

    x=var.get()
    if x==1:
        lst.append('MALE')
    else:
        lst.append('FEMALE')

    lst.append("\t")    

    x=passe4.get()
    lst.append(x)
    lst.append("\t")

    lst.append(s)
    lst.append('\t')
    lst.append('1000')

    f.writelines(lst)
    f.write("\n")
    f.close()



        

    
def log():
    global accno
    global loginname
    global s

    f=open('data.txt','r')
    x=f.readlines()
   
    
    flag=0

    s=loginname.get()
    for i in x:
        
        
        if(s in i):
           
           flag=1
           break

    if(flag==1):
        mainpage("<Button-1>")

    else:
        tkinter.messagebox.showinfo("INVALID","Your account number is invalid..")
    f.close()
    
def loginfunc(event):
    global a
    global loginname 
    
    a=2
    windows.destroy()
    root1.destroy()
    global root3
    global window3

    root3=Tk()
    window3=Frame(root3,width=400,height=300,bg="lightblue")
    root3.title("Login")
    window3.pack()

    namelabel=Label(window3,text='Account:-\nNumber',bg='lightblue')
    namelabel.place(x=30,y=35)
    
    loginname=Entry(window3,width=20,fg='black',bg='white',font=('Arial',16))
    loginname.place(x=110,y=30)
    
    passlabel=Label(window3,text='Password:-',bg='lightblue')
    passlabel.place(x=30,y=70)
    
    passe4=Entry(window3,width=20,fg='black',bg='white',font=('Arial',16),show='*')
    passe4.place(x=110,y=65)

    login=Button(window3,text='Login',width=5,height=2,bg='red',fg='white',command=log)
    login.place(x=140,y=110)
    
  
    root3.mainloop()

def signupfunc(event):
    
    global a
    a=1
    windows.destroy()
    root1.destroy()
    global root2
    global window1
    
    root2=Tk()
    window1=Frame(root2,width=400,height=300,bg="lightblue")
    window1.pack()
    root2.title("Signup")
    namelabel=Label(window1,text='NAME:-',bg='lightblue')
    namelabel.place(x=30,y=35)

    global namee1
    global emaile2
    global phoe3
    global g1
    global g2
    global passe4
    global accno

    
    namee1=Entry(window1,width=20,fg='black',bg='white',font=('Arial',16))
    namee1.place(x=110,y=30)
    
    emaillabel=Label(window1,text='Email Id:-',bg='lightblue')
    emaillabel.place(x=30,y=75)
    
    emaile2=Entry(window1,width=20,fg='black',bg='white',font=('Arial',16))
    emaile2.place(x=110,y=70)

    pholabel=Label(window1,text='CONTACT:-',bg='lightblue')
    pholabel.place(x=30,y=115)

    phoe3=Entry(window1,width=20,fg='black',bg='white',font=('Arial',16))
    phoe3.place(x=110,y=110)
    
    genderlabel=Label(window1,text='GENDER:-',bg='lightblue')
    genderlabel.place(x=30,y=145)
    global var
    var=IntVar()
    g1=Radiobutton(window1,text='MALE',variable=var,value=1,bg='lightblue')
    g1.place(x=110,y=145)
    g2=Radiobutton(window1,text='FEMALE',variable=var,value=2,bg='lightblue')
    g2.place(x=175,y=145)
    

    passlabel=Label(window1,text='PASSWORD:-',bg='lightblue')
    passlabel.place(x=30,y=180)
    
    passe4=Entry(window1,width=20,fg='black',bg='white',font=('Arial',16),show='*')
    passe4.place(x=110,y=175)

    

    done=Button(window1,text='DONE',width=5,height=2,bg='red',fg='white')
    done.place(x=100,y=220)
    done.bind("<Button-1>",filewrite)
    

    
    submit=Button(window1,text='SUBMIT',width=5,height=2,bg='red',fg='white')
    submit.place(x=180,y=220)
    submit.bind("<Button-1>",mainpage)

    
    
  
    root2.mainloop()

def userclick(event):
    window.destroy()
    root.destroy()
    global root1
    global windows
    
    root1=Tk()
    
    windows=Frame(root1,width=400,height=300,bg="lightblue")
    root1.title("HSBC")

    logo1=PhotoImage(file="front.png")
    logo1label=Label(windows,image=logo1)
    logo1label.place(x=20,y=20)

    
    login=Button(windows,text='LOG IN',width=20,bg="blue",fg="white")
    login.bind("<Button-1>",loginfunc)
    login.place(x=10,y=250)

    signup=Button(windows,text="NEW USER",width=20,bg="blue",fg="white")
    signup.bind("<Button-1>",signupfunc)
    signup.place(x=205,y=250)
   
    windows.pack()
    root1.mainloop()
    





def show():

            global flag
            
            if(flag==1):
           
                 tkinter.messagebox.showinfo("PASSWORD","Your Password has been changed successfully..")
            elif(flag==0):
                 tkinter.messagebox.showinfo("PASSWORD","Your have entered incorrect previous password.Password change Failed..")      

def staffclick(event):
   global root10
   window.destroy()
   root.destroy()

   root10=Tk()
   
  
   

   root10.title("STAFF")
   windo=Frame(root10,width=600,height=500,bg="lightblue")
   windo.pack(side=TOP)

   photo=PhotoImage(file="stafff.png")
   label=Label(windo,image=photo)
   label.place(x=100,y=130)

   menu=Menu(root10)
   root10.config(menu=menu)

   def customerlist():
    
       windo1=Frame(root10,width=600,height=500,bg="lightblue")
       windo1.place(x=0,y=0)
       fo=open('data.txt','r')
       x=fo.readlines()
       x1=0;y1=0
       for i in x:
         
         if(i != "\n"): 
          t=Text(windo1,width=300,height=3,font=("Verdana",8,'bold'),fg="BLACK",bg="lightgreen",wrap=WORD)
          t.insert(END,i)
          t.place(x=x1,y=y1)
          y1=y1+40

       fo.close()

   submenu=Menu(menu)
   menu.add_cascade(label="Customer List",menu=submenu)
   submenu.add_command(label="VIEW",command=customerlist)
   submenu.add_command(label="EXIT",command=quit)


   def terms():
          
          windo2=Frame(root10,width=600,height=500,bg="lightblue")
          windo2.place(x=0,y=0)
          t=Text(windo2,width=400,height=200,font=("Verdana",8,'bold'),fg="BLACK",bg="lightgreen",wrap=WORD)
          t.insert(END,'''
Courses Eligible:

 a. Studies in India:
• Graduation, Post-graduation including regular technical
and professional Degree/Diploma courses conducted by
colleges/universities approved by UGC/ AICTE/IMC/Govt.
etc
• Regular Degree/ Diploma Courses conducted by
autonomous institutions like IIT, IIM etc
• Teacher training/ Nursing courses approved by Central
government or the State Government
• Regular Degree/Diploma Courses like Aeronautical, pilot
training, shipping etc. approved by Director General of
Civil Aviation/Shipping
• Vocational Training and skill development study courses
will not be covered under the Education Loan Scheme, as
the scheme is framed to provide bank loans for higher
studies.
\n b. Studies abroad:
• Graduation/ Post-graduation for job oriented
professional/ technical courses offered by reputed
universities 



Student Eligibility:
\n• Should be an Indian National
• Secured admission to Professional/Technical courses
through Entrance Test/Selection process.
• Secured admission to foreign university/Institutions.
• No minimum qualifying marks stipulated in the last
qualifying examination ''')
          t.place(x=0,y=0)

   submenu=Menu(menu)
   menu.add_cascade(label="Terms and Conditions on offers for HSBC Bank Personal Loans ",menu=submenu)
   submenu.add_command(label="VIEW",command=terms)
   submenu.add_command(label="EXIT",command=quit)


   def change():

       global windo3
       windo3=Frame(root10,width=600,height=500,bg="lightblue")
       windo3.place(x=0,y=0)
       fi=open('data.txt','r')
       

       previous=Label(windo3,text="Previous Password",bg='yellow',font=('Arial',16))
       entry1=Entry(windo3,width=20,fg='black',bg='lightgrey',font=('Arial',16),show="*")
       new=Label(windo3,text="New Password",bg='yellow',font=('Arial',16))
       entry2=Entry(windo3,width=20,fg='black',bg='lightgrey',font=('Arial',16),show="*")                                                      
       conform=Label(windo3,text="Conform Password",bg='yellow',font=('Arial',16))
       entry3=Entry(windo3,width=20,fg='black',bg='lightgrey',font=('Arial',16),show="*")

       previous.place(x=80,y=140)
       entry1.place(x=280,y=140)
       new.place(x=80,y=190)
       entry2.place(x=280,y=190)
       conform.place(x=80,y=240)
       entry3.place(x=280,y=240)              

       prev=entry1.get()
       new=entry2.get()

       global flag
       flag=0

       x=fi.readlines()
      
       for i in x:
           print(prev)
           print(i)
           if( prev in i):
               print(prev)
               flag=1
               break

       


       login=Button(windo3,text='OK',width=5,height=2,bg='red',fg='white',command=show)
       login.place(x=250,y=300)

       login=Button(windo3,text='Exit',width=5,height=2,bg='red',fg='white',command=quit)
       login.place(x=310,y=300)

       fi.close()


   submenu=Menu(menu)
   menu.add_cascade(label="ChangePassword ",menu=submenu)
   submenu.add_command(label="VIEW",command=change)
   submenu.add_command(label="EXIT",command=quit)


   root10.mainloop()

   






    
root=Tk()

window=Frame(root,width=600,height=500,bg="lightblue")
root.title("HSBC")

logo=PhotoImage(file="front.png")
logolabel=Label(window,image=logo)
logolabel.place(x=120,y=0)

t=Text(window,width=400,height=3,font=("Verdana",8,'bold'),fg="red",bg="yellow",wrap=WORD)
t.insert(END,"     HSBC never asks for confidential information such as PIN and OTP from customer.\n\t     Any such call can be made only by a fraudster.Please do not share personal info.")
t.place(x=0,y=100)

userimage=PhotoImage(file="staf.png")
userlabel=Label(window,image=userimage)
userlabel.place(x=50,y=180)


staffimage=PhotoImage(file="staff.png")
stafflabel=Label(window,image=staffimage)
stafflabel.place(x=330,y=180)

userbutton=Button(window,text="USERS",width=20,bg="blue",fg="white")
userbutton.bind("<Button-1>",userclick)
userbutton.place(x=70,y=430)

staffbutton=Button(window,text="STAFF",width=20,bg="blue",fg="white")
staffbutton.bind("<Button-1>",staffclick)
staffbutton.place(x=350,y=430)

window.pack()
root.mainloop()
