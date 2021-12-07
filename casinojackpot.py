from tkinter import *
from random import randint
root = Tk()
root.state('zoomed')
root.title("CASINO JACKPOT")
root.configure(bg='purple')
casino = Label(root, text="CASINO JACKPOT", font=("Broadway", 70),fg='orange', bg='purple')
casino.pack()
class Jackpot:
    def __init__(self):
        self.b = 1000
        self.bett = 0
        

    def clicked(self,guess):
        self.Random= randint(1,10)
        last = Toplevel(root)
        last.title=("RESULT")
        last.state('zoomed')
        Result=Label(last,font=("Stencil",45),bg="red")
        Result.place(x=625,y=100)
        Result1 = Label(last, text="THE NUMBER WAS : ",font=("Showcard Gothic", 20))
        Result1.place(x=600, y=270)
        Result2 = Label(last, text=self.Random, font=("Showcard Gothic", 20))
        Result2.place(x=900, y=270)
        Result3 = Label(last, text="YOU BALANCE IS : ", font=("Showcard Gothic", 20))
        Result3.place(x=625, y=380)
        Result4 = Label(last, font=("Showcard Gothic", 20))
        Result4.place(x=900, y=380)
        Result5 = Label(last, font=("Showcard Gothic", 20))
        Result5.place(x=505, y=325)
        Result6 = Label(last, font=("Showcard Gothic", 20))
        Result6.place(x=900, y=325)

        if self.Random==guess:
           self.b = self.b + self.bett
           Result.configure(text=" YOU WON! ",fg="black",bg="green")
           last.configure(bg="green")

           Result1.configure(bg="green")
           Result2.configure(bg="green")
           Result3.configure(bg="green")
           Result4.configure(text=self.b, bg="green")
           Result5.configure(text="YOU ARE CREDITED WITH : " ,bg="green")
           Result6.configure(text=self.bett, bg="green")
        else:
           self.b = self.b - self.bett
           Result.configure(text="YOU LOST!",fg="black",bg="red")
           last.configure(bg="red")

           Result2.configure(bg="red")
           Result3.configure(bg="red")
           Result4.configure(text=self.b,bg="red")
           Result5.configure(text="     YOU LOST THE AMOUNT : " , bg="red")
           Result6.configure(text=self.bett,bg="red")
           Result1.configure(bg="red")
        button1 = Button(last, text="PLAY AGAIN", bg='#03c03c', fg="white", font=("Britannic Bold", 15),
                         activebackground='white', command=obj.start)
    
        button1.place(x=660, y=550)
        button1.configure(height=2, width=20)
        button2 = Button(last, text="EXIT", bg='red', fg="white", font=("Britannic Bold", 15), activebackground='white',
                         command=lambda: obj.exit(root))
        
        button2.place(x=660, y=620)
        button2.configure(height=2, width=20)
    def start(self):
        if self.b>0:

            new = Toplevel(root)
            new.title("GAME")

            new.state('zoomed')
            new.configure(bg='#750000')
            title1 = Label(new, text="BET THE AMOUNT", font=("Stencil", 40),bg='#750000',fg="white",)
            title1.place(x=500 , y=10)
            Amount = Label(new, text='YOUR  CURRENT  BALANCE  IS  : ',fg="#daa520",font=("Showcard Gothic", 30), bg='#750000')
           
            Amount.place(x=385, y=200)
            Amount1 = Label(new, text=self.b, font=("Showcard Gothic", 30),fg="white", bg='#750000')
            
            Amount1.place(x=980, y=200)
            GuessLabel = Label(new, text="SELECT CERTAIN AMOUNT TO BET YOUR GUESS \nFROM THE FOLLOWING BOXES",fg="#daa520",
                           font=("Showcard Gothic", 25), bg='#750000')
            
            GuessLabel.place(x=380, y=350)
            btn1 = Button(new, text="100", bg="Blue", fg="white", width=4, height=1, font=('Helvetica', '20'),
                            command=lambda: obj.newroot(100))
            btn1.place(x=530,y=530)
            btn2 = Button(new, text="250", bg="Blue", fg="white", width=4, height=1, font=('Helvetica', '20'),
                      command=lambda: obj.newroot(250))
            btn2.place(x=630, y=530)
            btn3 = Button(new, text="500", bg="Blue", fg="white", width=4, height=1, font=('Helvetica', '20'),
                      command=lambda: obj.newroot(500))
            btn3.place(x=730, y=530)
            btn4= Button(new, text="750", bg="Blue", fg="white", width=4, height=1, font=('Helvetica', '20'),
                      command=lambda: obj.newroot(750))
            btn4.place(x=830, y=530)
            btn5 = Button(new, text="1000", bg="Blue", fg="white", width=4, height=1, font=('Helvetica', '20'),
                      command=lambda: obj.newroot(1000))
            btn5.place(x=930, y=530)
            button1 = Button(new, text="EXIT", bg='red', fg="black", font=("Britannic Bold", 10), activebackground='white',
                         command=lambda: obj.exit(root))
            
            button1.place(x=1350, y=110)
            button1.configure(height=2, width=10)
            button2 = Button(new, text="BACK", bg='red', fg="black", font=("Britannic Bold", 10), activebackground='white',
                                         command=lambda: obj.exit(new))
            
            button2.place(x=50, y=110)
            button2.configure(height=2, width=10)
        else:
            obj.exitt(root)
    def exitt(window):
        window.destroy()
        print("YOU CAN'T CONTINUE SINCE YOUR BALANCE IS ZERO\nTHANKS FOR PLAYING!")
    def newroot(self,bet):
        newroot = Toplevel(root)
        newroot.title("GAME")
        newroot.geometry("700x600")
        newroot.state('zoomed')
        newroot.configure(bg='black')
        title1 = Label(newroot, text="Guess a Number", font=("Stencil", 40), fg="#daa520",bg='black')
        title1.place(x=550 , y=10)
        BALANCE = Label(newroot, text="YOUR CURRENT BALANCE IS : ", font=("Showcard Gothic", 30), fg="white",bg='black')
       
        BALANCE.place(x=450, y=200)
        BALANCE1 = Label(newroot, text=self.b, font=("Broadway", 30),fg="white", bg='black')
        
        BALANCE1.place(x=1020, y=205)
        self.bett = bet
        INS = Label(newroot, text="TAP ON YOUR GUESS", font=("Showcard Gothic", 20), fg="white",
                        bg='black')
        INS.place(x=640, y=310)
        btn1 = Button(newroot, text="1", bg="skyBlue", fg="black", width=3, height=1, font=('Helvetica', '20'),
                      command=lambda: obj.clicked(1))
        btn1.place(x=600, y=400)
        btn2 = Button(newroot, text="2", bg="skyBlue", fg="black", width=3, height=1, font=('Helvetica', '20'),
                      command=lambda: obj.clicked(2))
        btn2.place(x=700, y=400)
        btn3 = Button(newroot, text="3", bg="skyBlue", fg="black", width=3, height=1, font=('Helvetica', '20'),
                      command=lambda: obj.clicked(3))
        btn3.place(x=800, y=400)
        btn4 = Button(newroot, text="4", bg="skyBlue", fg="black", width=3, height=1, font=('Helvetica', '20'),
                      command=lambda: obj.clicked(4))
        btn4.place(x=900, y=400)
        btn5 = Button(newroot, text="5", bg="skyBlue", fg="black", width=3, height=1, font=('Helvetica', '20'),
                      command=lambda: obj.clicked(5))
        btn5.place(x=600, y=500)
        btn6 = Button(newroot, text="6", bg="skyBlue", fg="black", width=3, height=1, font=('Helvetica', '20'),
                      command=lambda: obj.clicked(6))
        btn6.place(x=700, y=500)
        btn7 = Button(newroot, text="7", bg="skyBlue", fg="black", width=3, height=1, font=('Helvetica', '20'),
                      command=lambda: obj.clicked(7))
        btn7.place(x=800, y=500)
        btn8 = Button(newroot, text="8", bg="skyBlue", fg="black", width=3, height=1, font=('Helvetica', '20'),
                      command=lambda: obj.clicked(8))
        btn8.place(x=900, y=500)
        btn9 = Button(newroot, text="9", bg="skyBlue", fg="black", width=3, height=1, font=('Helvetica', '20'),
                      command=lambda: obj.clicked(9))
        btn9.place(x=700, y=600)
        btn10 = Button(newroot, text="10", bg="skyBlue", fg="black", width=3, height=1, font=('Helvetica', '20'),
                      command=lambda: obj.clicked(10))
        btn10.place(x=800, y=600)
        button1 = Button(newroot, text="EXIT", bg='red', fg="black", font=("Britannic Bold", 10), activebackground='white',
                         command=lambda: obj.exit(root))
        
        button1.place(x=1350, y=110)
        button1.configure(height=2, width=10)
        button2 = Button(newroot, text="BACK", bg='red', fg="black", font=("Britannic Bold", 10), activebackground='white',
                         command=lambda: obj.exit(newroot))
        
        button2.place(x=50, y=110)
        button2.configure(height=2, width=10)
    def exit(self,window):
        window.destroy()
    def rules(self):

        button.destroy()

        label1 = Label(root, text="THE RULES ARE : ", font=("Britannic Bold", 20),fg="white", bg="purple",)
        label2 = Label(root, text="1.GUESS A NUMBER BETWEEN 1 AND 10",bg="purple", fg="white",font=("Copper black", 15))
        label3 = Label(root, text="2.YOUR INITIAL AMOUNT WOULD BE 1000",fg="white", bg="purple",font=("Copper black", 15))
        label4 = Label(root, text="3.BET YOUR GUESS WITH CERTAIN AMOUNT",fg="white",bg="purple", font=("Copper black", 15))
        label5 = Label(root,
                       text="4.IF YOU GUESS THE CORRECT NUMBER , YOU WILL BE CREDITED WITH DOUBLE THE AMOUNT YOU BET",bg="purple",
                       fg="white",font=("Copper black", 15))
        label6 = Label(root, text="5.IF THE GUESS WAS WRONG ,THE BET AMOUNT WILL BE  DEDUCTED",bg="purple",
                       fg="white",font=("Copper black", 15))
        label7 = Label(root, text="6.YOU CAN PLAY THE GAME UNTIL YOUR AMOUNT BECOMES 0",bg="purple",fg="white", font=("Copper black", 15))
        label8 = Label(root, text="7.IF YOU WANT TO QUIT , PRESS 'EXIT'",fg="white", bg="purple",font=("Copper black", 15))
        label1.place(x=350, y=140)
        label2.place(x=350, y=180)
        label3.place(x=350, y=220)
        label4.place(x=350, y=260)
        label5.place(x=350, y=300)
        label6.place(x=350, y=340)
        label7.place(x=350, y=380)
        label8.place(x=350, y=420)
        button1 = Button(root, text="PLAY", bg='#03c03c', fg="white",font=("Britannic Bold",15),activebackground='white', command=obj.start)
        
        button1.place(x=580, y=550)
        button1.configure(height=2, width=20)
        button2 = Button(root, text="EXIT", bg='red',fg="white",font=("Britannic Bold",15), activebackground='white', command=lambda: obj.exit(root))
        
        button2.place(x=580, y=620)
        button2.configure(height=2, width=20)
        buttonn1.destroy()
        labeel.destroy()
obj = Jackpot()
buttonn1 = Button(root, text="START THE GAME", bg='green',font=("Britannic Bold",20), activebackground='white', command=obj.start)

buttonn1.place(x=600, y=480)
buttonn1.configure(height=2, width=20)
button = Button(root, text="DISPLAY THE RULES", bg='yellow',font=("Britannic Bold",20), activebackground='white', command=obj.rules)

button.configure(height=2, width=20)
button.place(x=600, y=250)
labeel = Label(root, text="OR",font=("Britannic Bold",25),bg="purple",fg="white")
labeel.place(x=710, y=380)
root.mainloop()
