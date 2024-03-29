def display_board(board):
    for row in board:
        print(" | ".join(row))
    print("-" * 9)

def check_winner(board, mark):
    for row in board:
        if all(cell == mark for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == mark for row in range(3)):
            return True
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
        return True
    return False

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        display_board(board)
        print(f"Player {current_player}'s turn")
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                break
            if check_draw(board):
                display_board(board)
                print("It's a draw!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("The selected cell is not empty. Please choose another cell.")

tic_tac_toe()
