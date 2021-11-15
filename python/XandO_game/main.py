# This is a script that accomplishes the tic-tac-toe game

from tkinter import *

root = Tk()
root.geometry("1200x900")

# code to verify which player is one or two

entry = Entry()
entry.grid(row=0, column=7)
player = entry.get()

# def check():


button = Button(text="submit")
button.grid(row=0, column=9)

buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
winner = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# ways x could win
ways = {"way_1": [[1, 1, 1], [0, 0, 0], [0, 0, 0]], "way_2": [[0, 0, 0], [1, 1, 1], [0, 0, 0]],
        "way_3": [[0, 0, 0], [0, 0, 0], [1, 1, 1]]
        }

count = 0

message = Label(text=" ")
message.grid(row=2, column=7)


def gamefunc(x, y):
    global count
    count = count + 1

    if count % 2 == 1:
        buttons[x][y].configure(text=" X ")
        winner[x][y] = 1
    if count % 2 == 0:
        buttons[x][y].configure(text=" O ")
        winner[x][y] = 2

    for m in range(3):
        for n in range(3):
            # print(winner[m][n])
            print(winner[m][n])
            print("----------------")
            print(ways["way_1"][m][n])
            print("=================")
            if winner == ways["way_1"]:
                message.configure(text="Player 1 won")
            else:
                message.configure(text=" ")

    # if winner[0][0] % 2 == 1 and winner[0][1] % 2 == 1 and winner[0][2] % 2 == 1:
    #     message.configure(text="Player 1 won")
    # else:
    #     message.configure(text="Player 2 won")
    # if winner[1][0] % 2 == 1 and winner[1][1] % 2 == 1 and winner[1][2] % 2 == 1:
    #     message.configure(text="Player 1 won")
    # else:
    #     message.configure(text="Player 2 won")
    # if winner[2][0] % 2 == 1 and winner[2][1] % 2 == 1 and winner[1][2] % 2 == 1:
    #     message.configure(text="Player 1 won")
    # else:
    #     message.configure(text="Player 2 won")
    # if winner[0][0] % 2 == 1 and winner[]


def reset(x):
    message.configure(text=" ")
    for k in range(3):
        for m in range(3):
            x[k][m].configure(text=" ")


for i in range(3):
    for j in range(3):
        buttons[i][j] = Button(text=" " * 5, font=("Verdana", 45), bg="yellow", width="3",
                               command=lambda x=i, y=j: gamefunc(x, y))
        buttons[i][j].grid(row=i, column=j)
# Reset Button
resetbutton = Button(text="reset", command=lambda x=buttons: reset(x))
resetbutton.grid(row=1, column=7)

mainloop()
