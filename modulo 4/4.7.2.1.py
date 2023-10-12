'''
  Nombre: Felipe Neri Francisco Bueno González
  Descripción:laboratorio: 4.7.2.1
'''

import random

def DisplayBoard(board):
    for row in board:
        print("+---+---+---+")
        print("|", end=" ")
        for cell in row:
            print(cell, "|", end=" ")
        print()
    print("+---+---+---+")

def EnterMove(board):
    while True:
        try:
            move = int(input("Ingresa tu movimiento (número del cuadro): "))
            if move < 1 or move > 9:
                raise ValueError("Número fuera de rango")
            row = (move - 1) // 3
            col = (move - 1) % 3
            if board[row][col] in ["O", "X"]:
                raise ValueError("Cuadro ocupado")
            board[row][col] = "O"
            break
        except (ValueError, IndexError):
            print("Movimiento inválido. Inténtalo de nuevo.")

def MakeListOfFreeFields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ["O", "X"]:
                free_fields.append((row, col))
    return free_fields

def VictoryFor(board, sign):
    for row in range(3):
        if all(board[row][col] == sign for col in range(3)):
            return True
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False

def DrawMove(board):
    free_fields = MakeListOfFreeFields(board)
    if free_fields:
        row, col = random.choice(free_fields)
        board[row][col] = "X"

def main():
    board = [["1", "2", "3"], ["4", "X", "6"], ["7", "8", "9"]]
    DisplayBoard(board)
    for _ in range(5):
        EnterMove(board)
        DisplayBoard(board)
        if VictoryFor(board, "O"):
            print("¡Has Ganado!")
            return
        if not MakeListOfFreeFields(board):
            print("¡Empate!")
            return
        DrawMove(board)
        DisplayBoard(board)
        if VictoryFor(board, "X"):
            print("La máquina ha ganado.")
            return
    print("¡Empate!")

if __name__ == "__main":
    main()
