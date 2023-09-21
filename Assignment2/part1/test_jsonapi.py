import unittest
from jsonapi import ExtendedEncoder, ExtendedDecoder

class TestJsonAPI(unittest.TestCase):

    def test_encode_decode_complex(self):
        complex_number = complex(1, 2)
        encoded = ExtendedEncoder().encode(complex_number)
        decoded = ExtendedDecoder().decode(encoded)
        self.assertEqual(complex_number, decoded)

    def test_encode_decode_range(self):
        range_obj = range(0, 10, 2)
        encoded = ExtendedEncoder().encode(range_obj)
        decoded = ExtendedDecoder().decode(encoded)
        self.assertEqual(list(range_obj), list(decoded))

if __name__ == "__main__":
    unittest.main()
