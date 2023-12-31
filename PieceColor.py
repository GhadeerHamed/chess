class PieceColor:
    color = None

    def __init__(self):
        self.color = None

    def __repr__(self):
        return self.color


class EmptyColor(PieceColor):
    def __init__(self):
        super().__init__()
        self.color = 'empty'


class White(PieceColor):
    def __init__(self):
        super().__init__()
        self.color = 'white'


class Black(PieceColor):
    def __init__(self):
        super().__init__()
        self.color = 'black'
