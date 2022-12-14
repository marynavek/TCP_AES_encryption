import random
import string
from sys import getsizeof
import unittest
from encryption_functions import encrypt_data, generate_key, decrypt_data

def randStr(chars = string.ascii_uppercase + string.digits, N=10):
	    return ''.join(random.choice(chars) for _ in range(N))

class TestEncryption(unittest.TestCase):

    def test_generate_key_same_input(self):
        user_input = "PASSWORD"
        generated_password = generate_key(user_input)
        self.assertEqual(generate_key(user_input), generated_password, "Should be {generated_password}")
    
    def test_generate_key_case_sensitive(self):
        user_input = "PASSWORD"
        user_input_1 = "password"
        generated_password = generate_key(user_input_1)
        self.assertNotEqual(generate_key(user_input), generated_password, "Should not be {generated_password}")

    def test_generate_key_return_size_and_type(self):
        user_input = "PASSWORD"
        self.assertEqual(len(generate_key(user_input)), 32, "Should be 512")
        self.assertEqual(type(generate_key(user_input)), bytes, "Should be bytes")

    def test_encrypt_data_same_key(self):
        original_data = "This is testing data"
        original_key = bytes(randStr(N=32), encoding='utf-8')
        encrypted_data = encrypt_data(original_data, original_key)
        self.assertNotEqual(encrypt_data(original_data, original_key), encrypted_data, "Should be Not the same")

    def test_encrypt_data_different_key(self):
        original_data = "This is testing data"
        original_key = bytes(randStr(N=32), encoding='utf-8')
        new_key =  bytes(randStr(N=32), encoding='utf-8')
        encrypted_data = encrypt_data(original_data, original_key)
        self.assertNotEqual(encrypt_data(original_data, new_key), encrypted_data, "Should be Not equal")

    def test_encrypt_data_different_data(self):
        original_data = "This is testing data"
        original_key = bytes(randStr(N=32), encoding='utf-8')
        new_data = "This is fake testing data"
        encrypted_data = encrypt_data(original_data, original_key)
        self.assertNotEqual(encrypt_data(new_data, original_key), encrypted_data, "Should be Not Equal ")

    def test_decrypt_data_same_key(self):
        original_data = "This is testing data."
        original_key = bytes(randStr(N=32), encoding='utf-8')
        encrypted_data = encrypt_data(original_data, original_key)
        decrypted_data = decrypt_data(encrypted_data, original_key)
        decoded_data = decrypted_data.decode("utf-8", errors='ignore')
        self.assertIn(original_data, decoded_data , "Should be True")

    def test_decrypt_data_different_key(self):
        original_data = "This is testing data."
        original_key = bytes(randStr(N=32), encoding='utf-8')
        fake_key =  bytes(randStr(N=32), encoding='utf-8')
        encrypted_data = encrypt_data(original_data, original_key)
        decrypted_data = decrypt_data(encrypted_data, fake_key)
        decoded_data = decrypted_data.decode("utf-8", errors='ignore')
        self.assertNotIn(original_data,decoded_data , "Should be False")


if __name__ == '__main__':
    unittest.main()