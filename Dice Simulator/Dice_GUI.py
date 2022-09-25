from cProfile import label
import random
from tkinter import *

root = Tk()
root.geometry("800x600")
root.title("Dice Simulator")

p1 = PhotoImage(file= 'dice.png')

root.iconphoto(False, p1)

l1 = Label(root, text="", font = ("times", 400))

def roll():
    number = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    l1.config(text=f'{random.choice(number)}{random.choice(number)}')
    l1.pack()

b1 = Button(root, text = "Lets ROLL...", font=("times", 10), command=roll)
b1.place(x=380,y=5)

root.mainloop()