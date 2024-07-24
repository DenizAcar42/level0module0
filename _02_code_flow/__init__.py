import random

def create_board(rows, cols, num_mines):
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    mine_positions = set()

    while len(mine_positions) < num_mines:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        mine_positions.add((row, col))

    for row, col in mine_positions:
        board[row][col] = '*'

    return board

def count_adjacent_mines(board, r, c):
    count = 0
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
            if board[nr][nc] == '*':
                count += 1

    return count

def reveal(board, revealed, rows, cols, r, c):
    if revealed[r][c]:
        return

    revealed[r][c] = True

    if board[r][c] == ' ':
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    reveal(board, revealed, rows, cols, nr, nc)

def print_board(board, revealed):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if revealed[r][c]:
                print(board[r][c], end=' ')
            else:
                print('.', end=' ')
        print()

def play_game(rows, cols, num_mines):
    board = create_board(rows, cols, num_mines)
    revealed = [[False for _ in range(cols)] for _ in range(rows)]
    game_over = False

    while not game_over:
        print_board(board, revealed)
        print("Enter row and column to reveal (e.g., 1 2): ")
        try:
            r, c = map(int, input().split())
            r -= 1  # convert to 0-indexed
            c -= 1  # convert to 0-indexed
        except ValueError:
            print("Invalid input. Please enter two numbers separated by space.")
            continue

        if not (0 <= r < rows and 0 <= c < cols):
            print("Out of bounds. Please enter valid coordinates.")
            continue

        if board[r][c] == '*':
            print("Game Over! You hit a mine.")
            revealed[r][c] = True
            game_over = True
        else:
            reveal(board, revealed, rows, cols, r, c)

        if all(all(revealed[r][c] or board[r][c] == '*' for c in range(cols)) for r in range(rows)):
            print_board(board, revealed)
            print("Congratulations! You win!")
            game_over = True

if __name__ == '__main__':
    rows = 8
    cols = 8
    num_mines = 10
    play_game(rows, cols, num_mines)
