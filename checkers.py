from minimaxtree import *


def check_move(tree, pawn, pawn_type, board):
    # wpisuje wszytskie możliwe ruchy do drzewa minimax
    if pawn_type == 'b':
        if pawn[0] < 9 and pawn[1] < 9:  # prawy dolny
            if board[pawn[1] + 1][pawn[0] + 1] == ' ':
                new_board = []
                for row in board:
                    new_board.append(row.copy())
                new_board[pawn[1]][pawn[0]] = ' '
                if pawn[1] + 1 == 9:
                    new_board[pawn[1] + 1][pawn[0] + 1] = create_king(pawn_type)
                else:
                    new_board[pawn[1] + 1][pawn[0] + 1] = pawn_type
                tree.insert(new_board, board)
        if pawn[0] > 0 and pawn[1] < 9:
            if board[pawn[1] + 1][pawn[0] - 1] == ' ':
                new_board = []
                for row in board:
                    new_board.append(row.copy())
                new_board[pawn[1]][pawn[0]] = ' '
                if pawn[1] + 1 == 9:
                    new_board[pawn[1] + 1][pawn[0] - 1] = create_king(pawn_type)
                else:
                    new_board[pawn[1] + 1][pawn[0] - 1] = pawn_type
                tree.insert(new_board, board)

    if pawn_type == 'w':
        if pawn[0] > 0 and pawn[1] > 0:  # lewy  górny
            if board[pawn[1] - 1][pawn[0] - 1] == ' ':
                new_board = []
                for row in board:
                    new_board.append(row.copy())
                new_board[pawn[1]][pawn[0]] = ' '
                if pawn[1] - 1 == 0:
                    new_board[pawn[1] - 1][pawn[0] - 1] = create_king(pawn_type)
                else:
                    new_board[pawn[1] - 1][pawn[0] - 1] = pawn_type
                tree.insert(new_board, board)
        if pawn[0] < 9 and pawn[1] > 0:  # prawy górny
            if board[pawn[1] - 1][pawn[0] + 1] == ' ':
                new_board = []
                for row in board:
                    new_board.append(row.copy())
                new_board[pawn[1]][pawn[0]] = ' '
                if pawn[1] - 1 == 0:
                    new_board[pawn[1] - 1][pawn[0] + 1] = create_king(pawn_type)
                else:
                    new_board[pawn[1] - 1][pawn[0] + 1] = pawn_type
                tree.insert(new_board, board)
    return tree


def check_mat(tree, current_board, fisrt_board, pawn, opponent, pawn_type, possible_moves):
    # wpisuje wszytskie możliwe zbicia do drzewa minimax, zwraca informację czy możliwe jest zbicie
    board = current_board
    mat = False
    # zmienna kontrolna, czy możliwe jest wykonanie kolejnego zbicia
    next_mat = False
    if pawn[0] < 8:
        if pawn[1] > 1 and 'r_u' in possible_moves:  # prawy górny
            if (board[pawn[1] - 1][pawn[0] + 1] in opponent) and board[pawn[1] - 2][pawn[0] + 2] == ' ':
                mat = True
                new_board = []
                for row in board:
                    new_board.append(row.copy())
                new_board[pawn[1]][pawn[0]] = ' '
                new_board[pawn[1] - 1][pawn[0] + 1] = ' '
                new_board[pawn[1] - 2][pawn[0] + 2] = pawn_type
                x = pawn[0] + 2
                y = pawn[1] - 2
                new_pawn = [x, y]
                tree, next_mat = check_mat(tree, new_board,fisrt_board, new_pawn, opponent, pawn_type, ['r_d', 'r_u', 'l_u'])
                if next_mat is False:
                    if y == 0 and pawn_type == 'w':
                        new_board[y][x] = create_king(pawn_type)
                    tree.insert(new_board, fisrt_board)
        if pawn[1] < 8 and 'r_d' in possible_moves:  # prawy dolny
            if (board[pawn[1] + 1][pawn[0] + 1] in opponent) and board[pawn[1] + 2][pawn[0] + 2] == ' ':
                mat = True
                new_board = []
                for row in board:
                    new_board.append(row.copy())
                new_board[pawn[1]][pawn[0]] = ' '
                new_board[pawn[1] + 1][pawn[0] + 1] = ' '
                new_board[pawn[1] + 2][pawn[0] + 2] = pawn_type
                x = pawn[0] + 2
                y = pawn[1] + 2
                new_pawn = [x, y]
                tree, next_mat = check_mat(tree, new_board, fisrt_board, new_pawn, opponent, pawn_type, ['r_d', 'r_u', 'l_d'])
                if next_mat is False:
                    if y == 9 and pawn_type == 'b':
                        new_board[y][x] = create_king(pawn_type)
                    tree.insert(new_board, fisrt_board)
    if pawn[0] > 1:
        if pawn[1] > 1 and 'l_u' in possible_moves:  # lewy  górny
            if (board[pawn[1] - 1][pawn[0] - 1] in opponent) and board[pawn[1] - 2][pawn[0] - 2] == ' ':
                mat = True
                new_board = []
                for row in board:
                    new_board.append(row.copy())
                new_board[pawn[1]][pawn[0]] = ' '
                new_board[pawn[1] - 1][pawn[0] - 1] = ' '
                new_board[pawn[1] - 2][pawn[0] - 2] = pawn_type
                x = pawn[0] - 2
                y = pawn[1] - 2
                new_pawn = [x, y]
                tree, next_mat = check_mat(tree, new_board, fisrt_board, new_pawn, opponent, pawn_type, ['r_u', 'l_d', 'l_u'])
                if next_mat is False:
                    if y == 0 and pawn_type == 'w':
                        new_board[y][x] = create_king(pawn_type)
                    tree.insert(new_board, fisrt_board)
        if pawn[1] < 8 and 'l_d' in possible_moves:  # lewy dolny
            if (board[pawn[1] + 1][pawn[0] - 1] in opponent) and board[pawn[1] + 2][pawn[0] - 2] == ' ':
                mat = True
                new_board = []
                for row in board:
                    new_board.append(row.copy())
                new_board[pawn[1]][pawn[0]] = ' '
                new_board[pawn[1] + 1][pawn[0] - 1] = ' '
                new_board[pawn[1] + 2][pawn[0] - 2] = pawn_type
                x = pawn[0] - 2
                y = pawn[1] + 2
                new_pawn = [x, y]
                tree, next_mat = check_mat(tree, new_board, fisrt_board, new_pawn, opponent, pawn_type, ['r_d', 'l_d', 'l_u'])
                if next_mat is False:
                    if y == 9 and pawn_type == 'b':
                        new_board[y][x] = create_king(pawn_type)
                    tree.insert(new_board, fisrt_board)
    return tree, mat


def check_mat_king(tree, current_board, fisrt_board, pawn, opponent, pawn_type, possible_directions):
    # wpisuje wszytskie możliwe zbicia do drzewa minimax, zwraca informację czy możliwe jest zbicie
    # zmienna possible_direction powstrzymuję pionek przed cofnięciem się
    board = current_board
    mat = False
    # zmienna kontrolna, czy możliwe jest wykonanie kolejnego zbicia
    next_mat = False
    if pawn[0] < 8:
        y = pawn[1]
        x = pawn[0]
        if 'r_u' in possible_directions:
            while y > 1 and x < 8 and (board[y - 1][x + 1] == ' ' or board[y - 1][x + 1] in opponent):  # prawy górny
                if board[y - 1][x + 1] in opponent and board[y - 2][x + 2] == ' ':
                    mat = True
                    new_board = []
                    for row in board:
                        new_board.append(row.copy())
                    new_board[pawn[1]][pawn[0]] = ' '
                    new_board[y - 1][x + 1] = ' '
                    new_board[y - 2][x + 2] = pawn_type
                    y = y - 2
                    x = x + 2
                    tree, next_mat = check_mat_king(tree, new_board, fisrt_board, [x, y], opponent, pawn_type, ['r_u', 'r_d', 'l_u'])
                    if next_mat is False:
                        while y >= 0 or x <= 9:
                            tree.insert(new_board, fisrt_board)
                            if y == 0 or x == 9 or new_board[y - 1][x + 1] != ' ':
                                break
                            new_board = []
                            for row in board:
                                new_board.append(row.copy())
                            new_board[pawn[1]][pawn[0]] = ' '
                            new_board[y - 1][x + 1] = pawn_type
                            y -= 1
                            x += 1

                    break
                if board[y - 1][x + 1] in opponent and board[y - 2][x + 2] != ' ':
                    break
                y -= 1
                x += 1
                if y == 0 or x == 9:
                    break

            y = pawn[1]
            x = pawn[0]
        if 'r_d' in possible_directions:
            while y < 8 and x < 8 and (board[y + 1][x + 1] == ' ' or board[y + 1][x + 1] in opponent):  # prawy dolny
                if board[y + 1][x + 1] in opponent and board[y + 2][x + 2] == ' ':
                    mat = True
                    new_board = []
                    for row in board:
                        new_board.append(row.copy())
                    new_board[pawn[1]][pawn[0]] = ' '
                    new_board[y + 1][x + 1] = ' '
                    new_board[y + 2][x + 2] = pawn_type
                    y = y + 2
                    x = x + 2
                    tree, next_mat = check_mat_king(tree, new_board, fisrt_board, [x, y], opponent, pawn_type, ['r_u', 'r_d', 'l_d'])
                    if next_mat is False:
                        while y <= 9 or x <= 9:
                            tree.insert(new_board, fisrt_board)
                            if y == 9 or x == 9 or new_board[y + 1][x + 1] != ' ':
                                break
                            new_board = []
                            for row in board:
                                new_board.append(row.copy())
                            new_board[pawn[1]][pawn[0]] = ' '
                            new_board[y + 1][x + 1] = pawn_type

                            y += 1
                            x += 1

                    break
                if board[y + 1][x + 1] in opponent and board[y + 2][x + 2] != ' ':
                    break
                y += 1
                x += 1
                if y == 9 or x == 9:
                    break
    if pawn[0] > 1:
        y = pawn[1]
        x = pawn[0]
        if 'l_u' in possible_directions:
            while y > 1 and  x > 1 and (board[y - 1][x - 1] == ' ' or board[y - 1][x - 1] in opponent):  # lewy  górny
                if board[y - 1][x - 1] in opponent and board[y - 2][x - 2] == ' ':
                    mat = True
                    new_board = []
                    for row in board:
                        new_board.append(row.copy())
                    new_board[pawn[1]][pawn[0]] = ' '
                    new_board[y - 1][x - 1] = ' '
                    new_board[y - 2][x - 2] = pawn_type
                    y = y - 2
                    x = x - 2
                    tree, next_mat = check_mat_king(tree, new_board, fisrt_board, [x, y], opponent, pawn_type, ['r_u', 'l_u', 'l_d'])
                    if next_mat is False:
                        while y >= 0 or x <= 0:
                            tree.insert(new_board, fisrt_board)
                            if y == 0 or x == 0 or new_board[y - 1][x - 1] != ' ':
                                break
                            new_board = []
                            for row in board:
                                new_board.append(row.copy())
                            new_board[pawn[1]][pawn[0]] = ' '
                            new_board[y - 1][x - 1] = pawn_type
                            y -= 1
                            x -= 1

                    break
                if board[y - 1][x - 1] in opponent and board[y - 2][x - 2] != ' ':
                    break
                y -= 1
                x -= 1
                if y == 0 or x == 0:
                    break
            y = pawn[1]
            x = pawn[0]
        if 'l_d' in possible_directions:
            while y < 8 and x > 1 and (board[y + 1][x - 1] == ' ' or board[y + 1][x - 1] in opponent):  # lewy dolny
                if board[y + 1][x - 1] in opponent and board[y + 2][x - 2] == ' ':
                    mat = True
                    new_board = []
                    for row in board:
                        new_board.append(row.copy())
                    new_board[pawn[1]][pawn[0]] = ' '
                    new_board[y + 1][x - 1] = ' '
                    new_board[y + 2][x - 2] = pawn_type
                    y = y + 2
                    x = x - 2
                    tree, next_mat = check_mat_king(tree, new_board, fisrt_board, [x, y], opponent, pawn_type, ['l_u', 'r_d', 'l_d'])
                    if next_mat is False:
                        while y <= 9 or x >= 0:
                            tree.insert(new_board, fisrt_board)
                            if y == 9 or x == 0 or new_board[y + 1][x - 1] != ' ':
                                break
                            new_board = []
                            for row in board:
                                new_board.append(row.copy())
                            new_board[pawn[1]][pawn[0]] = ' '
                            new_board[y + 1][x - 1] = pawn_type
                            y += 1
                            x -= 1

                    break
                if board[y + 1][x - 1] in opponent and board[y + 2][x - 2] != ' ':
                    break
                y += 1
                x -= 1
                if y == 9 or x == 0:
                    break

    return tree, mat


def check_move_king(tree, board, pawn, pawn_type):
    # wpisuje wszystkie możliwe ruchy do drzewa
    if pawn[0] < 9:
        y = pawn[1]
        x = pawn[0]
        while y > 0 and board[y - 1][x + 1] == ' ':  # prawy górny
            new_board = []
            for row in board:
                new_board.append(row.copy())
            new_board[pawn[1]][pawn[0]] = ' '
            new_board[y - 1][x + 1] = pawn_type
            tree.insert(new_board, board)

            y -= 1
            x += 1
            if y == 0 or x == 9:
                break

        y = pawn[1]
        x = pawn[0]
        while y < 9 and board[y + 1][x + 1] == ' ':  # prawy dolny
            new_board = []
            for row in board:
                new_board.append(row.copy())
            new_board[pawn[1]][pawn[0]] = ' '
            new_board[y + 1][x + 1] = pawn_type
            tree.insert(new_board, board)
            y += 1
            x += 1
            if y == 9 or x == 9:
                break
    if pawn[0] > 0:
        y = pawn[1]
        x = pawn[0]
        while y > 0 and board[y - 1][x - 1] == ' ':  # lewy  górny
            new_board = []
            for row in board:
                new_board.append(row.copy())
            new_board[pawn[1]][pawn[0]] = ' '
            new_board[y - 1][x - 1] = pawn_type
            tree.insert(new_board, board)
            y -= 1
            x -= 1
            if y == 0 or x == 0:
                break
        y = pawn[1]
        x = pawn[0]
        while y < 9 and board[y + 1][x - 1] == ' ':  # lewy dolny
            new_board = []
            for row in board:
                new_board.append(row.copy())
            new_board[pawn[1]][pawn[0]] = ' '
            new_board[y + 1][x - 1] = pawn_type
            tree.insert(new_board, board)
            y += 1
            x -= 1
            if y == 9 or x == 0:
                break
    return tree


def check_can_move(pawn, pawn_type, opponent, board):
    # sprawdzenie czy gracz nie został zablokowany
    if pawn_type == 'b' or pawn_type == 'b_k' or pawn_type == 'w_k':
        if pawn[0] < 9 and pawn[1] < 9:  # prawy dolny
            if board[pawn[1] + 1][pawn[0] + 1] == ' ':
                return True
        if pawn[0] > 0 and pawn[1] < 9:
            if board[pawn[1] + 1][pawn[0] - 1] == ' ':
                return True

    if pawn_type == 'w' or pawn_type == 'w_k' or pawn_type == 'b_k':
        if pawn[0] > 0 and pawn[1] > 0:  # lewy  górny
            if board[pawn[1] - 1][pawn[0] - 1] == ' ':
                return True
        if pawn[0] < 9 and pawn[1] > 0:  # prawy górny
            if board[pawn[1] - 1][pawn[0] + 1] == ' ':
                return True

    if pawn[0] < 8:
        if pawn[1] > 1:  # prawy górny
            if (board[pawn[1] - 1][pawn[0] + 1] in opponent) and board[pawn[1] - 2][pawn[0] + 2] == ' ':
                return True
        if pawn[1] < 8:  # prawy dolny
            if (board[pawn[1] + 1][pawn[0] + 1] in opponent) and board[pawn[1] + 2][pawn[0] + 2] == ' ':
                return True
    if pawn[0] > 1:
        if pawn[1] > 1:  # lewy  górny
            if (board[pawn[1] - 1][pawn[0] - 1] in opponent) and board[pawn[1] - 2][pawn[0] - 2] == ' ':
                return True
        if pawn[1] < 8:  # lewy dolny
            if (board[pawn[1] + 1][pawn[0] - 1] in opponent) and board[pawn[1] + 2][pawn[0] - 2] == ' ':
                return True
    return False


def check_win(board):
    # sparwdzenie czy graczowi pozostały pionki lub czy może wykonać ruch
    num_black = 0
    num_white = 0
    move_white = False
    move_black = False
    for row in range(len(board)):
        for i in range(len(board[row])):
            pawn = board[row][i]
            if pawn == 'w' or pawn == 'w_k':
                num_white += 1
                if check_can_move([i, row], pawn, ['b', 'b_k'], board) is True:
                    move_white = True

            if pawn == 'b' or pawn == 'b_k':
                num_black += 1
                if check_can_move([i, row], pawn, ['w', 'w_k'], board) is True:
                    move_black = True

    if move_white is False or num_white == 0:
        return True, 1
    if move_black is False or num_white == 0:
        return True, -1
    return False, 0


def create_king(pawn):
    if pawn == 'w':
        return 'w_k'
    if pawn == 'b':
        return 'b_k'


def control_num_moves(old_board, board, num_moves):
    # sprawdzenie czy wykonano zbicie
    old_pawns = []
    new_pawns = []
    for row_a in old_board:
        for a in row_a:
            old_pawns.append(a)
    for row_b in board:
        for b in row_b:
            new_pawns.append(b)
    old_pawns.sort()
    new_pawns.sort()
    if old_pawns == new_pawns:
        num_moves +=1
        return num_moves
    return 0
