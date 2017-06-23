import unittest

from model.model import Vector


class TestVector(unittest.TestCase):
    """Test Vector model"""

    def test_add(self):
        v1 = Vector(2, 3)
        v2 = Vector(2, 1)
        self.assertEqual(v1+v2, Vector(4, 4))

    def test_mul(self):
        v1 = Vector(2, 3)
        self.assertEqual(v1 * 3, Vector(6, 9))

    @unittest.skip("don't organization")
    def test_rmul(self):
        v1 = Vector(2, 3)
        self.assertEqual(3 * v1, Vector(6, 9))

    def test_abs(self):
        v1 = Vector(3, 4)
        self.assertEqual(abs(v1), 5)

    def test_abs_zero(self):
        v1 = Vector(0, 0)
        self.assertEqual(abs(v1), 0)

    def test_bool(self):
        v0 = Vector(0, 0)
        self.assertEqual(bool(v0), False)

        v1 = Vector(3, 4)
        self.assertEqual(bool(v1), True)


if __name__ == '__main__':
    unittest.main()