from logging import root
import tkinter as tk
import tkinter.font as tkFont


buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
buttonhandles = []
turn = 1
gameover = False


def buttonlabel(x):
    if x == 0:
        return ""
    if x == 1:
        return "X"
    if x == 2:
        return "O"

def buttoncolor(x):
    if x == 1:
        return "red"
    if x == 2:
        return "blue"

def click(r, k):
    global turn
    if buttons[r][k] != 0 or gameover == True:
        return
    if turn % 2 == 0:
        buttons[r][k] = 2
    else:
        buttons[r][k] = 1
    turn += 1
    buttonhandles[3*r+k]["text"] = buttonlabel(buttons[r][k])
    buttonhandles[3*r+k]["fg"] = buttoncolor(buttons[r][k])
    sjekk()


def win(winner):
    global gameover 
    gameover = True

    def end():
        winscreen.destroy()
        root.destroy()
    
    def restart():
        winscreen.destroy()
        global gameover
        gameover = False
        global turn
        turn = 1
        global buttons
        buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        global buttonhandles
        for b in buttonhandles:
            b["text"] = ""
    
    winscreen = tk.Tk()
    winscreen.title("Game Over")
    winscreen.geometry("150x100")

    if winner == "tie":
        wintext = tk.Label(winscreen, text="Tie!")
        wintext.pack()
    else:
        wintext = tk.Label(winscreen, text=winner+" has won!")
        wintext.pack()

    l = tk.Label(winscreen) 
    l.pack() #bare en placeholder fordi jeg ville ha litt mellomrom, vetke hvordan man ellers gjør det

    winscreenframe = tk.Frame(winscreen)
    winscreenframe.pack()

    close = tk.Button(winscreenframe, text="Close", command=end)
    close.pack(side=tk.LEFT)

    restart = tk.Button(winscreenframe, text="Restart", command=restart)
    restart.pack(side=tk.LEFT)

    winscreen.mainloop()

def fullt():
    global buttons
    for r in buttons:
        for e in r:
            if e == 0:
                return False
    return True

def sjekk():
    #sjekk x
    pass
    if buttons[2][0] == 1 and buttons[2][1] == 1 and buttons[2][2] == 1:
        win("X")
    elif buttons[1][0] == 1 and buttons[1][1] == 1 and buttons[1][2] == 1:
        win("X")
    elif buttons[0][0] == 1 and buttons[0][1] == 1 and buttons[0][2] == 1:
        win("X")

    elif buttons[2][0] == 1 and buttons[1][0] == 1 and buttons[0][0] == 1:
        win("X")
    elif buttons[2][1] == 1 and buttons[1][1] == 1 and buttons[0][1] == 1:
        win("X")
    elif buttons[2][2] == 1 and buttons[1][2] == 1 and buttons[0][2] == 1:
        win("X")

    elif buttons[0][0] == 1 and buttons[1][1] == 1 and buttons[2][2] == 1:
        win("X")
    elif buttons[2][0] == 1 and buttons[1][1] == 1 and buttons[0][2] == 1:
        win("X")

    #sjekk o
    elif buttons[2][0] == 2 and buttons[2][1] == 2 and buttons[2][2] == 2:
        win("O")
    elif buttons[1][0] == 2 and buttons[1][1] == 2 and buttons[1][2] == 2:
        win("O")
    elif buttons[0][0] == 2 and buttons[0][1] == 2 and buttons[0][2] == 2:
        win("O")

    elif buttons[2][0] == 2 and buttons[1][0] == 2 and buttons[0][0] == 2:
        win("O")
    elif buttons[2][1] == 2 and buttons[1][1] == 2 and buttons[0][1] == 2:
        win("O")
    elif buttons[2][2] == 2 and buttons[1][2] == 2 and buttons[0][2] == 2:
        win("O")

    elif buttons[0][0] == 2 and buttons[1][1] == 2 and buttons[2][2] == 2:
        win("O")
    elif buttons[2][0] == 2 and buttons[1][1] == 2 and buttons[0][2] == 2:
        win("O")

    #sjekk uavgjort
    elif fullt() == True:
        win("tie")
        
def game():
    global root
    root = tk.Tk()
    root.geometry('350x350')
    #root.configure(bg="green")
    root.title("tictactoe")

    fontStyle = tkFont.Font(family="Calibri", size=20)
    fontStyle2 = tkFont.Font(family="Calibri", size=75)

    title = tk.Label(root, text='Tic-Tac-Toe!', font=fontStyle)
    title.pack()

    board = tk.Frame(root)
    board.pack()

    row1 = tk.Frame(board)
    row1.pack()
    a1f = tk.Frame(row1)
    a1f.pack(side=tk.LEFT)
    a1b = tk.Button(a1f, fg="red", width=2, font=fontStyle2, text=buttonlabel(buttons[0][0]), command=lambda : click(0,0))
    a1b.pack()
    b1f = tk.Frame(row1)
    b1f.pack(side=tk.LEFT)
    b1b = tk.Button(b1f, fg="red", width=2, font=fontStyle2, text=buttonlabel(buttons[1][0]), command=lambda : click(1, 0))
    b1b.pack()
    c1f = tk.Frame(row1)
    c1f.pack(side=tk.LEFT)
    c1b = tk.Button(c1f, fg="red", width=2, font=fontStyle2, text=buttonlabel(buttons[2][0]), command=lambda : click(2, 0))
    c1b.pack()

    row2 = tk.Frame(board)
    row2.pack()
    a2f = tk.Frame(row2)
    a2f.pack(side=tk.LEFT)
    a2b = tk.Button(a2f, fg="red", width=2, font=fontStyle2, text=buttonlabel(buttons[0][1]), command=lambda : click(0, 1))
    a2b.pack()
    b2f = tk.Frame(row2)
    b2f.pack(side=tk.LEFT)
    b2b = tk.Button(b2f, fg="red", width=2, font=fontStyle2, text=buttonlabel(buttons[1][1]), command=lambda : click(1, 1))
    b2b.pack()
    c2f = tk.Frame(row2)
    c2f.pack(side=tk.LEFT)
    c2b = tk.Button(c2f, fg="red", width=2, font=fontStyle2, text=buttonlabel(buttons[2][1]), command=lambda : click(2, 1))
    c2b.pack()

    row3 = tk.Frame(board)
    row3.pack()
    a3f = tk.Frame(row3)
    a3f.pack(side=tk.LEFT)
    a3b = tk.Button(a3f, fg="red", width=2, font=fontStyle2, text=buttonlabel(buttons[0][2]), command=lambda : click(0, 2))
    a3b.pack()
    b3f = tk.Frame(row3)
    b3f.pack(side=tk.LEFT)
    b3b = tk.Button(b3f, fg="red", width=2, font=fontStyle2, text=buttonlabel(buttons[1][2]), command=lambda : click(1, 2))
    b3b.pack()
    c3f = tk.Frame(row3)
    c3f.pack(side=tk.LEFT)
    c3b = tk.Button(c3f, fg="red", width=2, font=fontStyle2, text=buttonlabel(buttons[2][2]), command=lambda : click(2, 2))
    c3b.pack()

    global buttonhandles
    buttonhandles = [a1b, a2b, a3b, b1b, b2b, b3b, c1b, c2b, c3b]

    root.mainloop()


game()