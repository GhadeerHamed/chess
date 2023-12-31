from PieceColor import PieceColor, White, Black, EmptyColor


class Piece:
    def __init__(self, color=PieceColor()):
        self.symbol = None
        self.color = color

    def __repr__(self):
        return self.symbol + self.color.color

    def is_valid_move(self, start_pos, end_pos, board):
        # Placeholder method, to be overridden by specific piece classes
        return False

    def _check_path_clear(self, start_pos, end_pos, board):
        return True

    def move(self, start_pos, end_pos, board):
        # Placeholder method, to be overridden by specific piece classes
        pass


class EmptyPiece(Piece):
    def __init__(self):
        super().__init__(EmptyColor())
        self.symbol = ' '


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'P'

    def is_valid_move(self, start_pos, end_pos, board):
        # Implement pawn's move validation logic
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        direction = -1 if isinstance(self.color, White) else 1
        opponent_color_type = Black if isinstance(self.color, White) else White

        # Pawn moves forward one square
        if start_col == end_col:
            if (start_row + direction == end_row
                    and isinstance(board[end_row][end_col], EmptyPiece)):
                return True

        elif end_col - 1 == start_col or end_col + 1 == start_col:
            if (start_row + direction == end_row
                    and isinstance(board[end_row][end_col].color, opponent_color_type)):
                return True
        return False

    def move(self, start_pos, end_pos, board):
        if self.is_valid_move(start_pos, end_pos, board):
            board[end_pos[0]][end_pos[1]] = board[start_pos[0]][start_pos[1]]
            board[start_pos[0]][start_pos[1]] = EmptyPiece()
            return True
        return False


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'B'

    def is_valid_move(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Check if the move is diagonal
        if abs(end_row - start_row) == abs(end_col - start_col):
            # Check for obstructions along the diagonal path
            direction_row = 1 if end_row > start_row else -1
            direction_col = 1 if end_col > start_col else -1

            check_row, check_col = start_row + direction_row, start_col + direction_col

            while check_row != end_row and check_col != end_col:
                if not isinstance(board[check_row][check_col], EmptyPiece):
                    return False
                check_row += direction_row
                check_col += direction_col

            # Check if the final position is empty or has an opponent's piece
            if isinstance(board[end_row][end_col], EmptyPiece) or \
                    board[end_row][end_col].color != self.color:
                return True

        return False

    def move(self, start_pos, end_pos, board):
        if self.is_valid_move(start_pos, end_pos, board):
            board[end_pos[0]][end_pos[1]] = board[start_pos[0]][start_pos[1]]
            board[start_pos[0]][start_pos[1]] = EmptyPiece()
            return True
        return False


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'N'

    def is_valid_move(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Knight moves in an L shape (2 squares in one direction and 1 square in another)
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)

        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)

    def move(self, start_pos, end_pos, board):
        if self.is_valid_move(start_pos, end_pos, board):
            board[end_pos[0]][end_pos[1]] = board[start_pos[0]][start_pos[1]]
            board[start_pos[0]][start_pos[1]] = EmptyPiece()
            return True
        return False


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'R'

    def is_valid_move(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Rook moves horizontally or vertically
        return (start_row == end_row or start_col == end_col) \
               and self._check_path_clear(start_pos, end_pos, board)

    def _check_path_clear(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Check if the path is clear for the Rook to move
        direction_row = 1 if end_row > start_row else (-1 if end_row < start_row else 0)
        direction_col = 1 if end_col > start_col else (-1 if end_col < start_col else 0)

        check_row, check_col = start_row + direction_row, start_col + direction_col

        while check_row != end_row or check_col != end_col:
            if not isinstance(board[check_row][check_col], EmptyPiece):
                return False
            check_row += direction_row
            check_col += direction_col

        return True

    def move(self, start_pos, end_pos, board):
        if self.is_valid_move(start_pos, end_pos, board):
            board[end_pos[0]][end_pos[1]] = board[start_pos[0]][start_pos[1]]
            board[start_pos[0]][start_pos[1]] = EmptyPiece()
            return True
        return False


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'Q'

    def is_valid_move(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Queen moves like a Rook or Bishop - horizontally, vertically, or diagonally
        return (start_row == end_row or start_col == end_col or
                abs(end_row - start_row) == abs(end_col - start_col)) \
               and self._check_path_clear(start_pos, end_pos, board)

    def _check_path_clear(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # Check if the path is clear for the Queen to move
        direction_row = 1 if end_row > start_row else (-1 if end_row < start_row else 0)
        direction_col = 1 if end_col > start_col else (-1 if end_col < start_col else 0)

        check_row, check_col = start_row + direction_row, start_col + direction_col

        while check_row != end_row or check_col != end_col:
            if not isinstance(board[check_row][check_col], EmptyPiece):
                return False
            check_row += direction_row
            check_col += direction_col

        return True

    def move(self, start_pos, end_pos, board):
        if self.is_valid_move(start_pos, end_pos, board):
            board[end_pos[0]][end_pos[1]] = board[start_pos[0]][start_pos[1]]
            board[start_pos[0]][start_pos[1]] = EmptyPiece()
            return True
        return False


class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = 'K'

    def is_valid_move(self, start_pos, end_pos, board):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        # King moves one square in any direction
        return abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1

    def move(self, start_pos, end_pos, board):
        if self.is_valid_move(start_pos, end_pos, board):
            board[end_pos[0]][end_pos[1]] = board[start_pos[0]][start_pos[1]]
            board[start_pos[0]][start_pos[1]] = EmptyPiece()
            return True
        return False