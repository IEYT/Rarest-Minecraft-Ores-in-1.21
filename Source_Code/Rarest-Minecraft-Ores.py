#Top #10 rarest minecraft ores in order(not including deepslate versions of ores).
    
    #Source  https://rarest.org/entertainment/rarest-ore-in-minecraft
from tkinter import *
Root = Tk()
Root.title('Rarest Mincraft ores')
Root.iconbitmap('Logo.ico')

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

# First Button #
def button1():
    label = Label(Root, text='The rarest one is the Emerald ore then,')
    label.grid(row=0, column=1)
#######################################################################
Button1  = Button(Root, text='1st', command=button1)
Button1.grid(row=0, column=0)
#######################################################################

# Second Button #
def button2():
    label2 = Label(Root, text='Ancient Debris then,')
    label2.grid(row=0, column=2)
#####################################################
Button2  = Button(Root, text='2nd', command=button2)
Button2.grid(row=2, column=1)
#####################################################

# Third Button #
def button3():
    label3 = Label(Root, text='Diamond ore then,')
    label3.grid(row=0, column=3)
##################################################
Button3 = Button(Root, text='3rd', command=button3)
Button3.grid(row=3, column=2)
##################################################

# Fourth Button #
def button4():
    label4 = Label(Root, text='Lapis Lazuli ore then,')
    label4.grid(row=0, column=4)
#######################################################
Button4  = Button(Root, text='4th', command=button4)
Button4.grid(row=4, column=3)
#######################################################

# Fifth Button #
def button5(): 
    label5 = Label(Root, text='Redstone ore then,')
    label5.grid(row=0, column=5)
###################################################
Button5  = Button(Root, text='5th', command=button5)
Button5.grid(row=5, column=4)
###################################################

# Sixth Button #
def button6():
    label6 = Label(Root, text='Nether Gold ore then,')
    label6.grid(row=0, column=6)
######################################################
Button6  = Button(Root, text='6th', command=button6)
Button6.grid(row=6, column=5)
######################################################

# Seventh Button #
def button7():
    label7 = Label(Root, text='Gold ore then,')
    label7.grid(row=0, column=7)
###############################################
Button7  = Button(Root, text='7th', command=button7)
Button7.grid(row=7, column=6)
###############################################

# Eighth Button #
def button8():
    label8 = Label(Root, text='Iron Ore then,')
    label8.grid(row=0, column=8)
###############################################
Button8  = Button(Root, text='8th', command=button8)
Button8.grid(row=8, column=7)
###############################################

# Ninth Button #
def button9():
    lable9 = Label(Root, text='Nether Quartz then')
    lable9.grid(row=0, column=9)
###################################################



# Tenth Button #
def button10():
    label10 = Label(Root, text="Copper ore, and that's it!")
    label10.grid(row=0, column=10)
#######################################################################
Button10 = Button(Root, text='10th', command=button10)
Button10.grid(row=10, column=9)
#######################################################################

Root.mainloop()
