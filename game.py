from random import randint
from time import sleep

board = [[1,2,3],
        [4,5,6],
        [7,8,9]]




win = [[1,2,3],
        [4,"X",6],
        [7,8,9],
        [1,4,7],
        [2,"X",8],
        [3,6,9],
        [1,"X",9],
        [3,"X",7]
]

choices = [1,2,3,4,5,6,7,8,9]

endgame = 0


def winner():
    global endgame
    #print("Será que alguém venceu???")
    for indicelin, col in enumerate(win):          # i = índice da linha, row = a linha (ex: [1,2,3])
        #print(win[indicelin][0],win[indicelin][1],win[indicelin][2])
        if win[indicelin][0] == win[indicelin][1] == win[indicelin][2]:
            print("WINNER!!! The winner is:", win[indicelin][0])
            endgame = 1
"""        else:
            print("LOSER")"""




def show_board():
    print(f"""
+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+
""")



def yourturn():
    print("It's your turn!!!")
    found = 0
    while found == 0:
        try:
            number = int(input("Pick a position: "))
            choices.remove(number)
            print("Choices:",choices)

            # MUDANÇA DE VALOR NO BOARD
            while True:
                for indicelin, col in enumerate(board):          # i = índice da linha, row = a linha (ex: [1,2,3])
                    if number in col:
                        indicecol = col.index(number)            # j = índice do número dentro da linha
                        #print(f"Número encontrado na posição: linha {indicelin}, coluna {indicecol}")
                        board[indicelin][indicecol] = "O"
                        show_board()
                        found = 1
                        break
                found = 1
                break

            # MUDANÇA DE VALOR NA TABELA DE WIN
            while True: 
                for indicelin, col in enumerate(win):          # i = índice da linha, row = a linha (ex: [1,2,3])
                    if number in col:
                        indicecol = col.index(number)            # j = índice do número dentro da linha
                        #print(f"Número encontrado na posição: linha {indicelin}, coluna {indicecol}")
                        win[indicelin][indicecol] = "O"
                break
            break
            #print("ESTOU PRESO NO LOOP WIN")
        except:
            print("Ops. Valor inválido, insira um válor numérico!")
            continue



def myturn():
    print("Now it's my turn!!!")
    try:

        ## GERAR UM NÚMERO AUTOMÁTICO
        while True:
            number = randint(1,10)
            #print("Number:",number)
            if number in choices:
                choices.remove(number)
                break

        # ALTERAÇÃO DE VALOR DO BOARD
        while True:
            for indicelin, col in enumerate(board):          # i = índice da linha, row = a linha (ex: [1,2,3])
                if number in col:
                    indicecol = col.index(number)            # j = índice do número dentro da linha
                    #print(f"Número encontrado na posição: linha {indicelin}, coluna {indicecol}")
                    board[indicelin][indicecol] = "X"
                    show_board()
                    found = True
                    break
            break

        # MUDANÇA DE VALOR NA TABELA DE WIN
        while True: 
            for indicelin, col in enumerate(win):          # i = índice da linha, row = a linha (ex: [1,2,3])
                if number in col:
                    indicecol = col.index(number)            # j = índice do número dentro da linha
                    #print(f"Número encontrado na posição: linha {indicelin}, coluna {indicecol}")
                    win[indicelin][indicecol] = "X"
                    found = 1
            found = 1
            break
        


    except:
        print("DEU RUIM")




##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################

print("WELCOME TO TIC TAC TO!!!")
show_board()
print("I will be the X and you will be O!!!\nI will start!")

sleep(2)
while True:
    answer = input("Are you ready? ")
    if answer != "":
        break

board[1][1] = "X"
choices.remove(5)
#print("Choices:",choices)
show_board()

while True:

    yourturn()
    winner()
    sleep(2)
    #print("endgame", endgame)
    if endgame == 1:
        break

    myturn()
    winner()
    sleep(2)
    #print("endgame", endgame)
    if endgame == 1:
        break
print("END GAME \n THANK YOU FOR PLAYING")