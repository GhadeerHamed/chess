from PieceColor import Black, White
from Pieces import Bishop, Knight, Pawn, King, Rook, Queen, EmptyPiece


def initialize_board():
    board = [
        [Rook(Black()), Knight(Black()), Bishop(Black()), Queen(Black()), King(Black()), Bishop(Black()), Knight(Black()), Rook(Black())],
        [Pawn(Black()) for _ in range(8)],
        [EmptyPiece() for _ in range(8)] * 4,
        [Pawn(White()) for _ in range(8)],
        [Rook(White()), Knight(White()), Bishop(White()), Queen(White()), King(White()), Bishop(White()), Knight(White()), Rook(White())],
    ]
    return board


class ChessGame:
    def __init__(self):
        self.board = initialize_board()

    def display_board(self):
        for row in self.board:
            print(' '.join([piece.symbol for piece in row]))
