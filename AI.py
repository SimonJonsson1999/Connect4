class AI:
    def __init__(self, turn,  depth):
        self.depth = depth 
        self.turn = turn
    def choose_move(self, board, player):
        self.ai_player = player
        _, column = self.minimax(board, self.depth, True)
        return column

    def minimax(self, board, depth, maximizingPlayer):
        if depth == 0 or board.is_full() or board.checkwin(self.ai_player) or board.checkwin(-self.ai_player):
            return self.scoring(board, depth), None
        
        if maximizingPlayer:
            maxEval = float('-inf')
            best_col = None
            for col in range(board.ncols): 
                if board.is_valid_location(col):
                    temp_board = board.copy()
                    temp_board.move(col, self.ai_player)
                    eval, _ = self.minimax(temp_board, depth - 1, False)
                    if eval > maxEval:
                        maxEval = eval
                        best_col = col
            return maxEval, best_col
        else:
            minEval = float('inf')
            worst_col = None
            for col in range(board.ncols):
                if board.is_valid_location(col):
                    temp_board = board.copy()
                    temp_board.move(col, -self.ai_player)
                    eval, _ = self.minimax(temp_board, depth - 1, True)
                    if eval < minEval:
                        minEval = eval
                        worst_col = col
            return minEval, worst_col


    def scoring(self, board, depth):
        if board.checkwin(self.ai_player):
            return 10 - depth
        elif board.checkwin(-self.ai_player):
            return depth - 10
        else:
            return 0
