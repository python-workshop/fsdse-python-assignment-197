from unittest import TestCase


class TestMultiply(TestCase):
    def test_multiply(self):
        try:
            from build import multiply
        except ImportError:
            self.assertFalse("no function found")

        self.assertEqual(2500, multiply(100, 25))
        self.assertEqual(0, multiply(100, 0))

    def test_subtract(self):
        try:
            from build import subtract
        except ImportError:
            self.assertFalse("no function found")

        self.assertEqual(75, subtract(100, 25))
        self.assertEqual(100, subtract(100, 0))
        self.assertEqual(200, subtract(100, -100))
        self.assertEqual(-200, subtract(-100, 100))
