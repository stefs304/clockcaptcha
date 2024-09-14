
import unittest
import random
from clockcaptcha import ClockCaptcha
from clockcaptcha.config import Config



class TestClockcaptcha(unittest.TestCase):

    def test_value(self):
        random.seed(0)
        captcha = ClockCaptcha()
        self.assertIsInstance(captcha.value, str)
        self.assertEqual(captcha.value, '1248')

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

