from totem.pieces.star_piece import StarPiece


class PieceManager:
    def __init__(self):
        self.piece_list = []
        self.piece_size = (101, 101)
        self.border_thickness = 2
        self.piece_color = (40, 100, 255)
        self.border_color = (210, 210, 210)

    def spawn_star(self, surface, middle_point, star_points):
        piece_1 = StarPiece(surface=surface,
                            size=self.piece_size,
                            middle_point=middle_point,
                            border_thickness=self.border_thickness,
                            border_color=self.border_color,
                            piece_color=self.piece_color,
                            star_points=star_points)
        piece_1.draw()

