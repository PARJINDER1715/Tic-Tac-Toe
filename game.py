import random

def is_winner(board, player):
    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6),
            (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(board[i] == board[j] == board[k] == player for i, j, k in wins)

def is_draw(board):
    return all(cell != "" for cell in board)

def minimax(board, is_maximizing):
    if is_winner(board, "O"):
        return 1
    elif is_winner(board, "X"):
        return -1
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == "":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = ""
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == "":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = ""
                best_score = min(score, best_score)
        return best_score

def random_move(board):
    empty = [i for i in range(9) if board[i] == ""]
    return random.choice(empty) if empty else -1

def best_move(board, difficulty="Hard"):
    if difficulty == "Easy":
        return random_move(board)
    elif difficulty == "Medium":
        return random_move(board) if random.random() < 0.5 else minimax_best_move(board)
    else:  # Hard
        return minimax_best_move(board)

def minimax_best_move(board):
    best_score = -float('inf')
    move = -1
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                move = i
    return move