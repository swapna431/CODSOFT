import math
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join([str(cell) if cell is not None else " " for cell in row]) + " |")
def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]             
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] is not None:
            return board[combo[0]]
    return None
def is_board_full(board):
    return all(cell is not None for cell in board)
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == 'X':
        return -10 + depth
    elif winner == 'O':
        return 10 - depth
    elif is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] is None:
                board[i] = 'O'
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = None
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] is None:
                board[i] = 'X'
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = None
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval
def best_move(board):
    best_val = -math.inf
    move = None
    for i in range(9):
        if board[i] is None:
            board[i] = 'O'
            move_val = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = None
            if move_val > best_val:
                best_val = move_val
                move = i
    return move
def play_game():
    board = [None] * 9
    current_turn = 'X'
    print_board(board)

    while True:
        if current_turn == 'X':
            move = int(input("Enter your move (0-8): "))
            if board[move] is None:
                board[move] = 'X'
                if check_winner(board) or is_board_full(board):
                    break
                current_turn = 'O'
        else:
            move = best_move(board)
            board[move] = 'O'
            print("AI move:")
            print_board(board)
            if check_winner(board) or is_board_full(board):
                break
            current_turn = 'X'
        print_board(board)

    winner = check_winner(board)
    if winner:
        print(f"The winner is {winner}!")
    else:
        print("It's a tie!")
if __name__ == "__main__":
    play_game()
