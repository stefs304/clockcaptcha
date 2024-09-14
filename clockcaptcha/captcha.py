
from .config import Config
from .helpers import Picasso
from random import randint
from typing import Union


class ClockCaptcha:

    def __init__(self, color_mode='rgb', clock_mode=24, size=3):
        """
        Captcha generator.
        :param color_mode: 'rgb' or 'grayscale'
        :param clock_mode: 12-hour or 24-hour clock
        :param size: relative size of the image. See table for pixel sizes.
        """
        if color_mode not in ['rgb', 'grayscale']:
            raise ValueError('color_mode must be "rgb" or "grayscale"')
        if clock_mode not in [12, 24]:
            raise ValueError("Clock mode must be 12 or 24")
        if not isinstance(size, int) or size <= 0:
            raise ValueError("size must be an integer greater than 0")
        self.color_mode = color_mode
        self.clock_mode = clock_mode
        self.size = size
        self._values = None
        self.painter: Picasso = None
        self.generate_new()

    def generate_new(self):
        """Generate new captcha"""
        self._generate_values()
        self.painter = Picasso(self._values, self.size)

    def _generate_values(self):
        hour_range = [0, 12]
        if self.clock_mode == 24:
            hour_range = [0, 23]
        hours = randint(*hour_range)
        minutes = randint(0, 59)
        hours = ['0', str(hours)] if hours < 10 else [str(hours)[0], str(hours)[1]]
        minutes = ['0', str(minutes)] if minutes < 10 else [str(minutes)[0], str(minutes)[1]]
        self._values = [*hours, *minutes]

    @property
    def value(self):
        return ''.join(self._values)

    def verify(self, value: Union[list[str], str]) -> bool:
        """Verify captcha"""
        if isinstance(value, list):
            value = ''.join(value)
        return self.value == value

    def save_image(self, path, format=None, **kwargs):
        """
        Save captcha image. Format inferred from file extension.
        :param path: path to file.
        :param format: If not provided, format inferred from file extension.
        If no file extension is provided, ValueError raised.
        :param kwargs: kwargs to pillow's Image.save() method
        :return:
        """
        if self.color_mode == 'grayscale':
            self.painter.image = self.painter.image.convert('L')
        self.painter.image.save(path, format=format, **kwargs)

    @staticmethod
    def set_colors(colors: list[str]):
        """
        Set colors.
        :param colors: list of hex colors. len >= 2
        :return:
        """
        if len(colors) < 2:
            raise ValueError('Must have at least 2 colors')
        Config.colors = colors

