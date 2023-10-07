#Top #10 rarest minecraft ores in order(not including deepslate versions of ores).
    
    #Source  https://rarest.org/entertainment/rarest-ore-in-minecraft
from tkinter import *
Root = Tk()
Root.iconbitmap('Logo.ico')
Root.title('Rarest Mincraft ores')


#First =   ('The best one is the Emerald ore then,')
#Second =  ('Ancient Debris then,')
#Third =   ('Diamond ore')
#Fourth =  ('Gold ore')
#Fifth =   ('Redstone ore')
#Sixth =   ('Lapis Lazuli ore')
#Seventh = ('Iron ore')
#Eighth =  ('Copper Ore')
#Ninth =   ('Coal ore')
#Tenth =   ('Nether Gold ore')   

def button1():
    label = Label(Root, text='The rarest one is the Emerald ore then,')
    label.grid(row=0, column=1)

def button2():
    label2 = Label(Root, text='Ancient Debris then,')
    label2.grid(row=0, column=2)

def button3():
    label3 = Label(Root, text='Diamond ore then,')
    label3.grid(row=0, column=3)

def button4():
    label4 = Label(Root, text='Lapis Lazuli ore then,')
    label4.grid(row=0, column=4)

def button5(): 
    label5 = Label(Root, text='Redstone ore then,')
    label5.grid(row=0, column=5)

def button6():
    label6 = Label(Root, text='Nether Gold ore then,')
    label6.grid(row=0, column=6)

def button7():
    label7 = Label(Root, text='Gold ore then,')
    label7.grid(row=0, column=7)

def button8():
    label8 = Label(Root, text='Iron Ore then,')
    label8.grid(row=0, column=8)

def button9():
    lable9 = Label(Root, text='Nether Quartz then')
    lable9.grid(row=0, column=9)

def button10():
    label10 = Label(Root, text="Copper ore, and that's it!")
    label10.grid(row=0, column=10)


Root.mainloop()
