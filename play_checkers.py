import math
import statistics
from checkers import *


def possible_mat_moves(tree, board, pawns, opponent):
    # sparwdza czy możliwe jest wykonanie ruchu zbijajacego, jeśli tak algorytm musi go wykonanć
    mat = False
    mat_k = False
    stop = False
    for row in range(len(board)):
        for i in range(len(board[row])):
            pawn = board[row][i]
            if pawn == pawns[0]: #x_k
                tree, mat_k = check_mat_king(tree, board, board, [i, row], opponent, pawns[0], ['r_u', 'r_d', 'l_u', 'l_d'])
                if mat_k is True:
                    stop = True

            if pawn == pawns[1]: #x
                tree, mat = check_mat(tree, board, board, [i, row], opponent, pawns[1], ['r_u', 'r_d', 'l_u', 'l_d'])
                if mat is True:
                    stop = True
    return tree, stop


def possible_moves(tree, board, pawns):
    # jeśli nie ma ruchów zbijających wyszukuje wszytskie możliwe ruchy
    for row in range(len(board)):
        for i in range(len(board[row])):
            pawn = board[row][i]
            if pawn == pawns[0]:
                tree = check_move_king(tree, board, [i, row], pawns[0])

            if pawn == pawns[1]:
                tree = check_move(tree, [i, row], pawns[1], board)
    return tree


def move_pawns(tree, board, pawns, opponent):
    # wyszukiwanie wszystkich możliwych ruchów
    tree, mat = possible_mat_moves(tree, board, pawns, opponent)
    if mat is True:
        return tree
    else:
        tree = possible_moves(tree, board, pawns)
    return tree


def create_minimax_tree(d, array, board):
    # stworzenie drzewa z wszytskimi możliwymi ruchami do poziomu d
    tree = MINIMAX_tree()
    tree.insert(board, None)
    mat = False
    mat_k = False
    first = array[0]
    second = array[1]
    tree = move_pawns(tree, board, first, second)
    new_boards = tree.find_children([tree.root])
    d -=1
    while d != 0:
        # wyszukiwanie kolejnych potomków
        for b in new_boards:
            tree = move_pawns(tree, b.value, second, first)
        d -= 1
        if d == 0:
            break
        new_boards = tree.find_children(new_boards)

        for b in new_boards:
            tree = move_pawns(tree, b.value, first, second)
        d -= 1
        if d == 0:
            break
        new_boards = tree.find_children(new_boards)
    return tree


def minimax_alpha_beta(tree, depth, node, maximizing_player, alpha, beta):

    if depth == 0 or check_win(node.value)[0]:
        return tree.calculate_score(node), tree

    if maximizing_player:
        best = -math.inf

        for i in node.children:
            val, tree = minimax_alpha_beta(tree, depth - 1, i, False, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        tree.set_score(node, best)
        return best, tree

    else:
        best = math.inf

        for i in node.children:

            val, tree = minimax_alpha_beta(tree, depth - 1, i, True, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break
        tree.set_score(node, best)
        return best, tree


def white_move(d, board):
    tree = create_minimax_tree(d, [['w_k', 'w'], ['b_k', 'b']], board)
    score, tree = minimax_alpha_beta(tree, d, tree.root, False, -math.inf, math.inf)
    # wykonanie następnego ruchu na podstawie oceny
    board = tree.move(score)
    win, winner = check_win(board.value)
    return win, winner, board.value


def black_move(d, board):
    tree = create_minimax_tree(d, [['b_k', 'b'], ['w_k', 'w']], board)
    score, tree = minimax_alpha_beta(tree, d, tree.root, True, -math.inf, math.inf)
    board = tree.move(score)
    win, winner = check_win(board.value)
    return win, winner, board.value


def print_array(array):
    for r in array:
        for c in r:
            print(c, end=" ")
        print()
    print('=======================')


def play(d, second_d):
    # num_moves - wartość kontrolna ruchów, sluży do uniknięcia zapętlenia
    num_moves = 0
    win = False

    board = [[' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],
             ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
             [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],
             ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w'],
             ['w', ' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w', ' '],
             [' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w'],
             ['w', ' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w', ' ']]
    while win is False:
        old_board = []
        for row in board:
            old_board.append(row.copy())
        win, winner, board = white_move(second_d, board)
        num_moves = control_num_moves(old_board, board, num_moves)
        if win is True:
            print_array(board)
            return winner,board
        if num_moves > 20:
            print_array(board)
            return 0, board
        old_board = []
        for row in board:
            old_board.append(row.copy())
        win, winner, board = black_move(d, board)
        num_moves = control_num_moves(old_board, board, num_moves)
        if win is True:
            print_array(board)
            return winner, board
        if num_moves > 20:
            print_array(board)
            return 0, board


def calculate_winner(array):
    white = 0
    black = 0
    draw = 0
    score = 0
    for i in array:
        score += i
        if i == 1:
            black +=1
        if i == -1:
            white += 1
        if i == 0:
            draw += 1
    print(f'black win: {black}, white win: {white}, draw: {draw}. Average:  {score/len(array)}')


def different_depth(d,second_d):
    winner_deeper_white = []
    winner_deeper_black = []
    winner_same_depth = []
    for i in range(10):
        winner, board = play(d, second_d)
        winner_deeper_white.append(winner)
    for j in range(10):
        winner, board = play(second_d, d)
        winner_deeper_black.append(winner)
    for k in range(10):
        winner, board = play(d, d)
        winner_same_depth.append(winner)
    print(f'results for the search with depth - white: {second_d}, black: {d}')
    calculate_winner(winner_deeper_white)
    print(f'results for the search with depth - white: {d}, black: {second_d}')
    calculate_winner(winner_deeper_black)
    print(f'results for the search with the same depth - {d}')
    calculate_winner(winner_same_depth)


different_depth(2, 3)

