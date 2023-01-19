#  Создайте программу для игры в ""Крестики-нолики"".
#  3*3

carta = [1,2,3,
        4,5,6,
        7,8,9]
 
pobeda = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]
 
def print_carta():
    print(carta[0], end = " ")
    print(carta[1], end = " ")
    print(carta[2])
    print(carta[3], end = " ")
    print(carta[4], end = " ")
    print(carta[5])
    print(carta[6], end = " ")
    print(carta[7], end = " ")
    print(carta[8])    
 
def step_carta(step,symbol):
    ind = carta.index(step)
    carta[ind] = symbol
 
def get_result():
    pob = ""
 
    for i in pobeda:
        if carta[i[0]] == "X" and carta[i[1]] == "X" and carta[i[2]] == "X":
            pob = "X"
        if carta[i[0]] == "O" and carta[i[1]] == "O" and carta[i[2]] == "O":
            pob = "O"   
             
    return pob
 
game_over = False
player1 = True
 
while game_over == False:
 
    print_carta()
 
    if player1 == True:
        symbol = "X"
        step = int(input(f"Первый игрок {symbol} ходит: "))
    else:
        symbol = "O"
        step = int(input(f"Второй игрок {symbol} ходит: "))
 
    step_carta(step,symbol) 
    pob = get_result() 
    if pob != "":
        game_over = True
    else:
        game_over = False
 
    player1 = not(player1)        

print_carta()
print("Выиграл", pob)