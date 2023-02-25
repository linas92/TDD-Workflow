import unittest

def encrypt(message):
    encrypted_message = [idx for idx, char in enumerate(message)]
    print(encrypted_message)
    return encrypted_message

class TestEncryption(unittest.TestCase):
    def setUp(self):
        self.my_message = "banana"
    def test_inputExists(self):
        self.assertIsNotNone(self.my_message)

    def test_inputType(self):
        self.assertIsInstance(self.my_message, str)

    def test_functionReturnsSometing(self):
        self.assertIsNotNone(encrypt(self.my_message))

    def test_lenIO(self):
        self.assertEqual(len(self.my_message), len(encrypt(self.my_message)))

    def test_differentIO(self):
        self.assertNotIn(self.my_message, encrypt(self.my_message))

    if __name__=="__main__":
        unittest.main()