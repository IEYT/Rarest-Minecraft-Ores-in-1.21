#Top #10 rarest minecraft ores in order(not including deepslate versions of ores).
    #Source  https://rarest.org/entertainment/rarest-ore-in-minecraft
    #Background  https://wallpaperaccess.com/rainbow-stripes
                # {Note, i am using a list from Minecraft version 1.20 because I couldn't find one for 1.21, so be aware that some of them might be wrong.}
from tkinter import *
Root = Tk()
Root.title('Rarest Mincraft ores')
Root.iconbitmap("Source_Code\Logo.ico") 
Root.geometry("1600x750")

Grid.columnconfigure(Root,0,weight=1)
Grid.columnconfigure(Root,1,weight=1) 

bg = PhotoImage(file="Source_Code\wobniar.png")
MyLabel = Label(Root, image=bg)
MyLabel.place(x=0, y=0, relwidth=1, relheight=1)

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
    label = Label(Root, text="The rarest one is the Emerald ore then,", bg="red")
    label.grid(row=0, column=1)

Button1  = Button(Root, text='1st', command= button1, bg="blue")
Button1.grid(row=0, column=0, sticky="NSEW")


# Second Button #
def button2():
    label2 = Label(Root, text="Ancient Debris then,", bg="orange")
    label2.grid(row=1, column=2)

Button2  = Button(Root, text='2nd', command= button2, bg='#007FFF') # #007FFF = Random light blue
Button2.grid(row=1, column=1, sticky="NSEW")


# Third Button #
def button3():
    label3 = Label(Root, text="Diamond ore then,", bg="yellow")
    label3.grid(row=2, column=1)

Button3 = Button(Root, text='3rd', command= button3, bg='blue')
Button3.grid(row=3, column=0, sticky="NSEW")


# Fourth Button #
def button4():
    label4 = Label(Root, text="Gold ore then,", bg="#aff8bf") # #aff8bf = Random generated light green
    label4.grid(row=4, column=2)

Button4  = Button(Root, text='4th', command= button4, bg="#CBC3E3") # #CBC3E3 = Random light purple
Button4.grid(row=4, column=1, sticky="NSEW")


# Fifth Button #
def button5(): 
    label5 = Label(Root, text="Redstone ore then,", bg="blue")
    label5.grid(row=5, column=1)
Button5 = Button(Root, text='5th', command= button5, bg='red')
Button5.grid(row=5, column=0, sticky="NSEW")


# Sixth Button #
def button6():
    label6 = Label(Root, text="Lapis Lazuli then,", bg="#4B0082") # #4B0082 = Indigo.
    label6.grid(row=6, column=2)

Button6  = Button(Root, text='6th', command= button6, bg='#378200') # #378200 = shade of Office green
Button6.grid(row=6, column=1, sticky="NSEW")


# Seventh Button #
def button7():
    label7 = Label(Root, text="Iron ore then,", bg="purple")
    label7.grid(row=7, column=1)

Button7  = Button(Root, text='7th', command= button7, bg='#008000') # #008000 = Office green
Button7.grid(row=7, column=0, sticky="NSEW")


# Eighth Button #
def button8():
    label8 = Label(Root, text="Copper ore then,", bg="#7F00FF") # #7F00FF = Violet
    label8.grid(row=8, column=2)

Button8  = Button(Root, text='8th', command= button8, bg='#80FF00') # #80FF00 = Highlighter green/ Neon green
Button8.grid(row=8, column=1, sticky="NSEW")


# Ninth Button #
def button9():
    lable9 = Label(Root, text="Coal then", bg="#b7d2f9") # #b7d2f9 = Random generated light blue
    lable9.grid(row=9, column=1)

Button9 = Button(Root, text='9th', command= button9, bg='#482d06') # #482d06 = shade of brown
Button9.grid(row=9, column=0, sticky="NSEW")


# Tenth Button #
def button10():
    label10 = Label(Root, text="Nether Gold, and that's it!", bg="green")
    label10.grid(row=10, column=2)

Button10 = Button(Root, text='10th', command= button10, bg='magenta')
Button10.grid(row=10, column=1, sticky="NSEW")

Root.mainloop()
##
