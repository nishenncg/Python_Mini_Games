from tkinter import *
import random

#Gui window
root = Tk()
root.geometry('400x400')
root.resizable(0, 0)
root.title('ROCK PAPER SCISSOR GAME')
root.config(bg='cyan')
Label(root, text='Rock Paper Scissor Game', font='arial 15 bold').pack()


user_take = StringVar()
Label(root, text='choose any one: rock, paper ,scissor', font='arial 15 bold').place(x=20, y=70)
Entry(root, font = 'arial 12', textvariable = user_take).place(x=90, y=130)

comp_pick = random.randint(1, 3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick == 2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissor'


Result = StringVar()
def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('tie,Damn it is the same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you loose,It is paper bby')
    elif user_pick == 'rock' and comp_pick == 'scissor':
        Result.set('you win,oh no i got knoked')
    elif user_pick == 'paper' and comp_pick == 'scissor':
        Result.set('you loose,It is scissor bby')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win,the rock jst let me down')
    elif user_pick == 'scissor' and comp_pick == 'rock':
        Result.set('you loose,you got knoked dear')
    elif user_pick == 'scissor' and comp_pick == 'paper':
        Result.set('you win ,you tared me apart')
    else:
        Result.set('invalid: choose any given moron haha')

def Reset():
    Result.set("")
    user_take.set("")

def Exit():
    root.destroy()

Entry(root, font='arial 10 bold', textvariable=Result, width=50, ).place(x=25, y=250)
Button(root, font='arial 12 bold', text='Play', padx=5, command=play).place(x=150, y=190)
Button(root, font='arial 12 bold', text='Reset', padx=5, command=Reset).place(x=70, y=310)
Button(root, font='arial 12 bold', text='Exit', padx=5, command=Exit).place(x=230, y=310)
root.mainloop()
