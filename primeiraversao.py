from random import randint

board = [[1,2,3],
        [4,5,6],
        [7,8,9]]

choices = [1,2,3,4,5,6,7,8,9]



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
    try:
        number = int(input("Pick a position: "))
        choices.remove(number)
        print("Choices:",choices)

        while True:
            for indicelin, col in enumerate(board):          # i = índice da linha, row = a linha (ex: [1,2,3])
                if number in col:
                    indicecol = col.index(number)            # j = índice do número dentro da linha
                    print(f"Número encontrado na posição: linha {indicelin}, coluna {indicecol}")
                    board[indicelin][indicecol] = "O"
                    show_board()
                    found = True
                    break
            break

    except:
        print("Ops. Valor inválido, insira um válor numérico!")



def myturn():
    print("Now it's my turn!!!")
    try:
        while True:
            number = randint(1,10)
            print("Number:",number)
            if number in choices:
                choices.remove(number)
                break
            else:
                print("TRY AGAIN")
        print("Choices:",choices)
        while True:
            for indicelin, col in enumerate(board):          # i = índice da linha, row = a linha (ex: [1,2,3])
                if number in col:
                    indicecol = col.index(number)            # j = índice do número dentro da linha
                    print(f"Número encontrado na posição: linha {indicelin}, coluna {indicecol}")
                    board[indicelin][indicecol] = "X"
                    show_board()
                    found = True
                    break
            break
    except:
        print("LITERALMENTE CHEGAR AQUI DEVERIA SER IMPOSSÍVEL")



##################################################################################################
##################################################################################################
print("WELCOME TO TIC TAC TO!!!")
show_board()
print("I will be the X and you will be O!!!")
board[1][1] = "X"
choices.remove(5)
print("Choices:",choices)
show_board()
yourturn()
myturn()
yourturn()
myturn()
yourturn()
myturn()