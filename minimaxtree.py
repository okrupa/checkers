import random


class Node:
    def __init__(self, value):
        self.children = []
        self.value = value
        self.score = None


class MINIMAX_tree:
    def __init__(self):
        self.root = None

    def insert(self, value, parent):
        if self.root is None:
            board = Node(value)
            self.root = board
        else:
            self._insert(value, parent, self.root)

    def _insert(self, value, parent,  node):
            if parent == node.value:
                new_board = Node(value)
                node.children.append(new_board)
                return
            else:
                for i in node.children:
                    self._insert(value, parent, i)

    def find_children(self, node):
        childrens = []
        for n in node:
            for i in n.children:
                childrens.append(i)
        return childrens

    def move(self, score):
        node = self.root
        moves = []
        for i in node.children:
            if i.score == score:
                moves.append(i)
        return random.choice(moves)

    def score_pawn(self, pawn, pawn_king, num, board, opponent):
        score = 0
        pawns_num = 0
        for i in range(5):
            for j in board[i]:
                if j == pawn:
                    score += num[0]
                    pawns_num += 1
                if j == pawn_king:
                    score += 10
                    pawns_num += 1
                if j in opponent:
                    pawns_num += 1
        for i in range(5, 10):
            for j in board[i]:
                if j == pawn:
                    score += num[1]
                    pawns_num += 1
                if j == pawn_king:
                    score += 10
                    pawns_num += 1
                if j in opponent:
                    pawns_num += 1
        if pawns_num == 0:
            pawns_num = 1
        return score/pawns_num

    def score(self, board):
        white_score = self.score_pawn('w', 'w_k', [7, 5], board, ['b', 'b_k'])
        black_score = self.score_pawn('b', 'b_k', [5, 7], board, ['w', 'w_k'])
        return black_score - white_score

    def calculate_score(self, node):
        if node == self.root:
            self.root,score = self.score(self.root.value)
            return self.root,score
        else:
            score = self._calculate_score(self.root, node)
            return score

    def _calculate_score(self, curr_node, node):
        if curr_node.value == node.value:
            curr_node.score = self.score(curr_node.value)
            return curr_node.score
        else:
            for i in curr_node.children:
                score = self._calculate_score(i, node)
                if score is not None:
                    return score

    def set_score(self, node, score):
        if node == self.root:
            self.root.score = score
        else:
            score = self._set_score(self.root, node, score)

    def _set_score(self, curr_node, node, new_score):
        if curr_node.value == node.value:
            curr_node.score = new_score
            return curr_node.score
        else:
            for i in curr_node.children:
                score = self._set_score(i, node, new_score)
                if score is not None:
                    return
