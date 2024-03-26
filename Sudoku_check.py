board = []


for x in range(9):
    numero = input(f"Digite os 9 numeros da linha {x+1} :")
    aux = []
    for y in range(9):
        aux.append(int(numero[y]))
    board.append(aux)

print()
for linha in board:
    print (linha)
print()

def check_linhas(board):
    for x in range(9):
        aux=[]
        for y in range(9):
            if board[x][y] not in aux:
                aux.append(board[x][y])
            else:
                print(f"Erro na linha {x} coluna {y}")
                return False
    return True
 
def check_colunas(board):
    for linha in range(9): #usado 
        aux = []
        for coluna in range(9):
            if board[coluna][linha] not in aux:
                aux.append(board[coluna][linha])
            else:
                print(f"Erro na coluna {coluna} linha {linha}")
                return False
    return True

def check_quadrante(board):
    
    #CHECA O QUADRANTE 1
    aux = []
    for x in range(3):
        for y in range(3):
            if board[x][y] not in aux:
                aux.append(board[x][y])
            else:
                print(f"Erro no Quadrante 1, Linha {x+1} coluna {y+1}")
                return False
                break
    
    #CHECA O QUADRANTE 2
    aux = []
    for x in range(3):
        for y in range(3,6):
            if board[x][y] not in aux:
                aux.append(board[x][y])
            else:
                print(f"Erro no Quadrante 2, Linha {x+1} coluna {y+1}")
                return False
                break

    #CHECA O QUADRANTE 3
    aux = []
    for x in range(3):
        for y in range(6,9):
            if board[x][y] not in aux:
                aux.append(board[x][y])
            else:
                print(f"Erro no Quadrante 3, Linha {x+1} coluna {y+1}")
                return False
                break
    
    #CHECA O QUADRANTE 4
    aux = []
    for x in range(3,6):
        for y in range(3):
            if board[x][y] not in aux:
                aux.append(board[x][y])
            else:
                print(f"Erro no Quadrante 4, Linha {x+1} coluna {y+1}")
                return False
                break
   
    #CHECA O QUADRANTE 5
    aux = []
    for x in range(3,6):
        for y in range(3,6):
            if board[x][y] not in aux:
                aux.append(board[x][y])
            else:
                print(f"Erro no Quadrante 5, Linha {x+1} coluna {y+1}")
                return False
                break
    
    #CHECA O QUADRANTE 6
    aux = []
    for x in range(3,6):
        for y in range(6,9):
            if board[x][y] not in aux:
                aux.append(board[x][y])
            else:
                print(f"Erro no Quadrante 6, Linha {x+1} coluna {y+1}")
                return False
                break

    #CHECA O QUADRANTE 7
    aux = []
    for x in range(6,9):
        for y in range(3):
            if board[x][y] not in aux:
                aux.append(board[x][y])
            else:
                print(f"Erro no Quadrante 7, Linha {x+1} coluna {y+1}")
                return False
                break            
    
    #CHECA O QUADRANTE 8
    aux = []
    for x in range(6,9):
        for y in range(3,6):
            if board[x][y] not in aux:
                aux.append(board[x][y])
            else:
                print(f"Erro no Quadrante 8, Linha {x+1} coluna {y+1}")
                return False
                break     
    
    #CHECA O QUADRANTE 8
    aux = []
    for x in range(6,9):
        for y in range(6,9):
            if board[x][y] not in aux:
                aux.append(board[x][y])
            else:
                print(f"Erro no Quadrante 8, Linha {x+1} coluna {y+1}")
                return False
                break     
    
    return True


print("Agora vamos Validar o SUDOKU: ")
if check_linhas(board):
    if check_colunas(board):
        if check_quadrante(board):
            print("PARABENS! SUDOKU VALIDADO!")
