
import unittest
import random
from color_captcha import ClockCaptcha
from color_captcha.config import Config
from tempfile import NamedTemporaryFile, TemporaryDirectory


class TestClockcaptcha(unittest.TestCase):

    def test_value(self):
        random.seed(0)
        captcha = ClockCaptcha()
        self.assertIsInstance(captcha.value, str)
        self.assertEqual(captcha.value, '1248')
        self.assertEqual(len(captcha.value), 4)

    def test_verify(self):
        random.seed(0)
        captcha = ClockCaptcha()
        print(captcha.value)
        self.assertTrue(captcha.verify('1248'))
        self.assertTrue(captcha.verify(['1', '2', '4', '8']))
        self.assertFalse(captcha.verify(1248))

    def test_set_colors(self):
        colors = ['#fff', '#000', '#f0f']
        ClockCaptcha.set_colors(colors)
        self.assertEqual(Config.colors, colors)
        with self.assertRaises(ValueError):
            ClockCaptcha.set_colors(['#fff', '#000'])
        with self.assertRaises(ValueError):
            ClockCaptcha.set_colors([])

    def test_save_file(self):
        captcha = ClockCaptcha()
        with NamedTemporaryFile() as f:
            self.assertIsNone(captcha.save_image(f, format='png'))
        with self.assertRaises(ValueError):
            captcha.save_image(f)
        with TemporaryDirectory() as tmp:
            file = f'{tmp}/image.png'
            self.assertIsNone(captcha.save_image(file))
            file = f'{tmp}/image.jpg'
            self.assertIsNone(captcha.save_image(file))

    def test_generate_new(self):
        random.seed(0)
        captcha = ClockCaptcha()
        self.assertTrue(captcha.verify('1248'))
        captcha.generate_new()
        self.assertNotEqual(captcha.value, '1248')
        self.assertIsInstance(captcha.value, str)
        self.assertEqual(len(captcha.value), 4)

