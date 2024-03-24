def evaluate(board):
    for player in [1, -1]:
        for i in range(3):
            if all(board[i][j] == player for j in range(3)) or \
               all(board[j][i] == player for j in range(3)):
                return player
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return player
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return player
    if all(cell != 0 for row in board for cell in row):
        return 0
    # No winner yet
    return None
# using MinMax Algo.
def minimax(board, depth, is_maximizing):
    winner = evaluate(board)
    if winner is not None:
     return winner * (10 - depth)  
    
    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:  
                    board[i][j] = 1  
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = 0  
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:  
                    board[i][j] = -1  
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = 0  
                    min_eval = min(min_eval, eval)
        return min_eval
def best_move(board):
    best_eval = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:  
                board[i][j] = 1
                eval = minimax(board, 0, False)
                board[i][j] = 0
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move
def print_board(board):
    for row in board:
        print(" | ".join(["X" if cell == 1 else "O" if cell == -1 else " " for cell in row]))
        print("---------")
def main():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    while evaluate(board) is None:
        print_board(board)
        while True:
            player_move = input("Enter your move (row col): ")
            try:
                row, col = map(int, player_move.split())
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if board[row][col] == 0:
                        break
                    else:
                        print("Invalid move! Cell already occupied. Try again.")
                else:
                    print("Invalid move! Row and column must be between 0 and 2. Try again.")
            except ValueError:
                print("Invalid input! Please enter two integers separated by space.")
        board[row][col] = -1
        if evaluate(board) is not None:
            break
        print("AI's move:")
        ai_move = best_move(board)
        board[ai_move[0]][ai_move[1]] = 1
    print_board(board)
    winner = evaluate(board)
    if winner == 0:
        print("It's a tie!")
    elif winner == 1:
        print("You lost!")
    else:
        print("Congratulations! You won!")
if __name__ == "__main__":
    main()
