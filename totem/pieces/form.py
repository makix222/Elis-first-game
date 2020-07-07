import pygame as py
from pygame.locals import *
import math


class PieceManager:
    def __init__(self):
        self.piece_list = []
        self.piece_size = (30, 30)
        self.border_thickness = 2
        self.piece_color = [color.THECOLORS.get('navy')]
        self.border_color = (210, 210, 210)

    def spawn_star(self, surface, middle_point, star_points):
        piece_1 = StarPiece(self.piece_size,
                            surface,
                            middle_point,
                            self.border_thickness,
                            self.border_color,
                            self.piece_color,
                            star_points)
        piece_1.draw()


class StarPiece:
    def __init__(self,
                 surface,
                 size: tuple,
                 middle_point: tuple,
                 border_thickness: int,
                 border_color,
                 piece_color,
                 star_points):
        self.surface = surface
        self.size = size
        self.middle_point = middle_point
        self.piece_color = piece_color
        self.border_thickness = border_thickness
        self.border_color = border_color
        self.star_points = star_points

        pos_left = self.middle_point[0] - int(size[0] / 2)
        pos_top = self.middle_point[1] - int(size[1] / 2)

        self.shape_size_rect = py.Rect((pos_left, pos_top), self.size)

        self.shape_size_weight = .95
        self.pointedness_weight = .2
        self.inner_radius = min(self.size) * self.pointedness_weight
        self.outside_radius = min(self.size) * self.shape_size_weight

        # Find points which make up entire circle.
        segment_angle = 360 / self.star_points
        outside_points = []
        self.star_point_lists = []
        for specific_point in range(0, self.star_points):
            specific_angle = specific_point * segment_angle
            mod_pos_x = self.outside_radius * math.cos(specific_angle)
            mod_pos_y = self.outside_radius * math.sin(specific_angle)
            position = (self.middle_point[0] + mod_pos_x, self.middle_point[1] + mod_pos_y)
            outside_points.append(position)

        for specific_point in range(0, self.star_points):
            specific_angle = specific_point * segment_angle - (segment_angle / 2)
            mod_pos_x = self.inner_radius * math.cos(specific_angle)
            mod_pos_y = self.inner_radius * math.sin(specific_angle)
            position = (self.middle_point[0] + mod_pos_x, self.middle_point[1] + mod_pos_y)
            self.star_point_lists.append(position)
            self.star_point_lists.append(outside_points[specific_point])

    def draw(self):
        # Draw border
        py.draw.rect(self.surface, self.border_color, self.shape_size_rect, self.border_thickness)
        # Draw center circle
        py.draw.polygon(self.surface, self.piece_color, self.star_point_lists, 1)

