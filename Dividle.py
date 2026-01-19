import tkinter
from random import randint
from time import sleep as wait

def hover(e):
    e.widget.config(bg=hoverColour)
def hover2(e):
    e.widget.config(bg=buttonColour)
    
def delete():
    for widget in window.winfo_children():
        widget.destroy()
        
def hide():
    #title.pack_forget()
    #button.place_forget()
    delete()
    fraction()

def centre(rX,rY,text,font):
    a = tkinter.Label(window,text=text,font=font)
    a.place(x=0,y=0)
    window.update_idletasks()
    offset = a.winfo_width()
    a.place(relx=rX,rely=rY,x=-offset/2)
    return a

def clear(list1,col):           #sets all number buttons back to grey (from red)
    for i in list1:
        i.config(bg=col)

def updateNum(cur):
    global outText
    outText = centre(0.5,.15,cur,("Arial",30))
    
def fraction():
    global cur, numberButtons
    global lives, score
    a = randint(1,98)
    b = randint(a+1,99)
    c = a/b                         #17? digits
    textNumber = tkinter.Label(window, text=f"{a}/{b} = ",font=("Arial",45))
    textNumber.pack()
    lives = 3
    score = 0
    livesText = tkinter.Label(window,text=f"Lives: {lives}",font=("Arial",20))
    livesText.place(x=20,rely=0.9)
    cur="0."
    updateNum(cur)
    numberButtons = numbers(c)

def numbers(c):
    a = []
    for i in range(0,10):
        b = tkinter.Button(window,text=f"{i}",command=lambda i=i: inpNumber(i,c),bg=buttonColour,activebackground=clickedColour,font=("Arial",30))
        b.place(relx = ((i%5)/5), rely = 0.4, y =+ ((i//5)*(numWidth+30)), x=+numGap, width=numWidth,height=numHeight)
        a.append(b)
    return (a)

def inpNumber(i,c):
    global cur, numberButtons
    global lives, score
    c = str(c)
    text = outText.cget("text")
    if len(text)+1 >= len(c):
        pass                                        #win
    else:
        nextDig = c[len(text)]
        print(nextDig,i,cur)                #devmode
        if int(nextDig)==i:
            clear(numberButtons,buttonColour)
            score+=1
            cur+=str(i)
            updateNum(cur)
        else:                                       #incorrect (noob)
            numberButtons[i].config(bg="red")
            lives -= 1
            livesText = tkinter.Label(window,text=f"Lives: {lives}",font=("Arial",20))
            livesText.place(x=20,rely=0.9)
            if lives <= 0:
                print("you lose")
                lose()
                pass                                #loss

def lose():
    global score
    delete()
    if score<3:
        losetext = "noob"
    elif score<6:
        losetext="mid"
    else:
        losetext="pro"
    loseText = centre(0.5,0.30,text="You lose",font=("Arial",60))
    loseText.config(fg="red")
    loseText2 = centre(0.5,0.47,text=f"Score: {score}",font=("Arial",30))
    loseText3 = centre(0.5,0.57,text=losetext,font=("Arial",27))
    
#label.config(text=textInput.get()+"F(x)")

#btn = tkinter.Button()
#for i,v in btn.config().items():
#    print(i,v)


window = tkinter.Tk()
window.title("Dividle")
window.geometry("900x600")
buttonWidth, buttonHeight = 350, 50
buttonColour = "#ABABAB"
hoverColour = "#CCCCCC"
clickedColour = "#C2C2C2"
numWidth,numHeight = 120,110
numGap = int(90-(numWidth)/2)

title = tkinter.Label(window,text="𝔻𝕚𝕧𝕚𝕕𝕝𝕖",font=("Arial",60))
title.pack()

button=tkinter.Button(window, text="Play", command=lambda: hide(),
                      bg = buttonColour, activebackground = clickedColour, font=("Arial",30))
button.place(relx = 0.5, rely=.4, width = buttonWidth, x =- buttonWidth/2, height = buttonHeight)
button.bind("<Enter>", hover)
button.bind("<Leave>", hover2)

button2=tkinter.Button(window, text="Play2", command=lambda: hide(),
                      bg = buttonColour, activebackground = clickedColour, font=("Arial",30))
button2.place(relx = 0.5, rely=.4, width = buttonWidth, x =- buttonWidth/2, height = buttonHeight,y=+(buttonHeight+5))
button2.bind("<Enter>", hover)
button2.bind("<Leave>", hover2)

#textInput=tkinter.Entry(window)
#textInput.pack()


window.mainloop()












