from time import sleep
from tkinter import *
import tkinter
from tracemalloc import start #import tất cả từ thư viên tkinter
from PIL import ImageTk , Image
from time import sleep
from pygame import *
img = [0,0,0]
game = Tk() #tạo cửa sổ game
game.title("Dino")
canvas = Canvas(master=game,width=600,height=300,background="white")
canvas.pack()
img[0] =ImageTk.PhotoImage(Image.open("human.png"))
img[1] =ImageTk.PhotoImage(Image.open("cloud.jpg"))
img[2] =ImageTk.PhotoImage(Image.open("tree.jpg"))

human=canvas.create_image(0,220,anchor=NW,image=img[0])
cloud=canvas.create_image(550,50,anchor=NW,image=img[1])
tree=canvas.create_image(550,250,anchor=NW,image=img[2])
canvas.update()
def moveCloud():
    global cloud
    canvas.move(cloud,-5,0)
    if canvas.coords(cloud)[0] <-20:
        canvas.delete(cloud)
        cloud=canvas.create_image(550,50,anchor=NW,image=img[1])
    canvas.update()
score=0
text_score = canvas.create_text(550,30,text="Score: "+ str(score),fill ="black",font=("Times",10))
def moveTree():
    global tree,score
    canvas.move(tree,-5,0)
    if canvas.coords(tree)[0] <-20:
        canvas.delete(tree)
        tree=canvas.create_image(550,250,anchor=NW,image=img[2])
        score += 1
        canvas.itemconfig(text_score,text="Score: "+ str(score))
    canvas.update()
check_jump = False
def jump():
    global check_jump
    if check_jump == False:
        check_jump = True
        for i in range(0,30):
            canvas.move(human,0,-5)
            moveCloud()
            moveTree()
            canvas.update()
            sleep(0.01)
        for i in range(0,30):
            canvas.move(human,0,5)
            moveCloud()
            moveTree()
            canvas.update()
            sleep(0.01)
        check_jump = False
def keyPress(event):
    if event.keysym == "space":
        jump()
canvas.bind_all("<KeyPress>",keyPress)       
gameover = False
def check_gameOver():
    global gameover
    if canvas.coords(tree)[0] <100 and canvas.coords(human)[1]>190:
        gameover = True
        text_gameover = canvas.create_text(300,150,text="Game Over ",fill ="red",font=("Times",30))
    game.after(100,check_gameOver)
check_gameOver()
while not gameover:
    moveCloud()
    moveTree()
    sleep(0.01)
game.mainloop()
