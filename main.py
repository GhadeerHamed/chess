import tkinter as tk
from PieceColor import Black, White
from Pieces import Bishop, Knight, Pawn, King, Rook, Queen, EmptyPiece

class ChessboardGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Chessboard")

        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        self.board = []  # Initialize board as an instance attribute

    def draw_board(self):
        for i in range(8):
            row = []
            for j in range(8):
                if (i + j) % 2 == 0:
                    color = "white"
                else:
                    color = "gray"

                x0, y0 = j * 50, i * 50
                x1, y1 = x0 + 50, y0 + 50

                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
                row.append(None)  # Initialize each square with None
            self.board.append(row)

    def draw_pieces(self, board):
        for row in range(8):  # Iterate over rows
            for col in range(8):  # Iterate over columns
                piece = board[row][col]
                if piece is not None:
                    x0, y0 = col * 50, row * 50
                    x1, y1 = x0 + 50, y0 + 50
                    self.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=piece.symbol, font=("Arial", 24))


def initialize_board():
    board = [
        [Rook(Black()), Knight(Black()), Bishop(Black()), Queen(Black()), King(Black()), Bishop(Black()), Knight(Black()), Rook(Black())],
        [Pawn(Black()) for _ in range(8)],
        [EmptyPiece() for _ in range(8)],
        [EmptyPiece() for _ in range(8)],
        [EmptyPiece() for _ in range(8)],
        [EmptyPiece() for _ in range(8)],
        [Pawn(White()) for _ in range(8)],
        [Rook(White()), Knight(White()), Bishop(White()), Queen(White()), King(White()), Bishop(White()), Knight(White()), Rook(White())],
    ]
    return board

def print_board(board):
    for row in board:
        for piece in row:
            if piece is None:
                print('-', end=' ')
            else:
                print(piece.symbol, end=' ')
        print()  # Move to the next line after printing each row


def main():
    root = tk.Tk()
    chessboard_gui = ChessboardGUI(root)

    chessboard_gui.draw_board()  # Draw the board squares
    board = initialize_board()   # Initialize the board
    chessboard_gui.draw_pieces(board)  # Draw the pieces
    root.mainloop()

if __name__ == "__main__":
    main()
