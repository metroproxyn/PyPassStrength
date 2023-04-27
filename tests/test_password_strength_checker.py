import unittest
# TODO: find more adequate name for the imported function
from password_strength_checker import password_strength_check

class TestPasswordStrengthCheck(unittest.TestCase):
    def test_weak_password(self):
        result = password_strength_check('password')
        self.assertEqual(result, 'Weak')

    def test_medium_password(self):
        result = password_strength_check('P@ssword123')
        self.assertEqual(result, 'Medium')

    def test_strong_password(self):
        result = password_strength_check('MyP@ssw0rd!sV3ryStr0ng') # actually not
        self.assertEqual(result, 'Strong')

    def test_invalid_password(self):
        result = password_strength_check('12345')
        self.assertEqual(result, 'Invalid')

if __name__ == '__main__':
    unittest.main()