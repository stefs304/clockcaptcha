
from .numbers import numbers, blank, sep
from .config import Config
from PIL import Image, ImageDraw
from random import randint



class Picasso:

    size = 10

    def __init__(self, values: list[str], size=3):
        self.grid = []
        self.values = values
        self.size = self.size * size
        width = int(19 * self.size)
        height = int(7 * self.size - self.size/2)
        self.image = Image.new('RGB', (width, height))
        self.canvas = ImageDraw.Draw(self.image)
        self.build_grid()
        self.paint()

    def build_grid(self):
        self.grid.append(TileGroup(blank, self.canvas, 0, self.size))
        self.grid.append(TileGroup(numbers[self.values[0]], self.canvas, self.size, self.size))
        self.grid.append(TileGroup(blank, self.canvas, 4*self.size, self.size))
        self.grid.append(TileGroup(numbers[self.values[1]], self.canvas, 5*self.size, self.size))
        self.grid.append(TileGroup(blank, self.canvas, 8*self.size, self.size))
        self.grid.append(TileGroup(sep, self.canvas, 9*self.size, self.size))
        self.grid.append(TileGroup(blank, self.canvas, 10*self.size, self.size))
        self.grid.append(TileGroup(numbers[self.values[2]], self.canvas, 11*self.size, self.size))
        self.grid.append(TileGroup(blank, self.canvas, 14*self.size, self.size))
        self.grid.append(TileGroup(numbers[self.values[3]], self.canvas, 15*self.size, self.size))
        self.grid.append(TileGroup(blank, self.canvas, 18*self.size, self.size))

    def paint(self):
        for tile_group in self.grid:
            tile_group.paint()


class TileGroup:

    def __init__(self, array, canvas, start_x, size):
        self.vertical_offset = randint(-int(size/2), 0)
        self.start_x = start_x
        self.start_y = 0
        self.size = size
        self.array = array
        self.canvas = canvas

    def paint(self):
        for i, row in enumerate(self.array):
            y_coord = self.start_y + i * self.size + self.vertical_offset
            for j, element in enumerate(row):
                x_coord = self.start_x + j * self.size
                colors = self._draw_base(x_coord, y_coord, self.size)
                if element:
                    self._draw_overlay(x_coord, y_coord, self.size, colors)

    def _draw_base(self, x, y, size):
        color_choices = list(Config.colors)
        used_colors = []
        color = color_choices[randint(0, len(color_choices)-1)]
        used_colors.append(color)
        color_choices.remove(color)
        self.canvas.rectangle([x, y, x+size, y+size], fill=color)
        color = color_choices[randint(0, len(color_choices)-1)]
        color_choices.remove(color)
        polygon_choices = [
            [(x, y), (x + size, y), (x + size, y + size)],
            [(x + size, y), (x + size, y + size), (x, y + size)],
        ]
        self.canvas.polygon(polygon_choices[randint(0, 1)], fill=color)
        return color_choices

    def _draw_overlay(self, x, y, size, colors):
        if colors:
            color = colors[randint(0, len(colors)-1)]
        else:
            color = Config.colors[randint(0, len(Config.colors)-1)]
        x, y = x + size/2, y + size/2
        radius = size/2
        self.canvas.circle((x, y), radius, fill=color)

