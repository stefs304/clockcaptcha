
import unittest
import random
from color_captcha import ClockCaptcha, DigitsCaptcha
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
        colors = ['#ffffff', '#000000', '#f0f0f0']
        ClockCaptcha.set_colors(colors)
        self.assertEqual(Config.colors, colors)
        with self.assertRaises(ValueError):
            ClockCaptcha.set_colors(['#fff', '#000'])
        with self.assertRaises(ValueError):
            ClockCaptcha.set_colors([])
        captcha = ClockCaptcha()
        self.assertEqual(len(captcha.value), 4)

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



class TestDigitsCaptcha(unittest.TestCase):

    def test_arguments(self):
        captcha = DigitsCaptcha(digits=4, color_mode='rgb', size=4)
        with self.assertRaises(ValueError):
            DigitsCaptcha(digits=0)
        with self.assertRaises(ValueError):
            DigitsCaptcha(size=0)
        with self.assertRaises(ValueError):
            DigitsCaptcha(color_mode='rgba')

    def test_value(self):
        random.seed(0)
        captcha = DigitsCaptcha()
        self.assertIsInstance(captcha.value, str)
        self.assertEqual(captcha.value, '6604')
        self.assertEqual(len(captcha.value), 4)

    def test_verify(self):
        random.seed(0)
        captcha = DigitsCaptcha()
        print(captcha.value)
        self.assertTrue(captcha.verify('6604'))
        self.assertTrue(captcha.verify(['6', '6', '0', '4']))
        self.assertFalse(captcha.verify(6604))

    def test_save_file(self):
        captcha = DigitsCaptcha()
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
        captcha = DigitsCaptcha()
        self.assertTrue(captcha.verify('6604'))
        captcha.generate_new()
        self.assertNotEqual(captcha.value, '6604')
        self.assertIsInstance(captcha.value, str)
        self.assertEqual(len(captcha.value), 4)
