from decode import *
import unittest

class testDecode(unittest.TestCase):

    def test_decode_string(self):
        string_to_decode = 'SGVsbG8sIFdvcmxkIQ=='
        expected_result = b'Hello, World!'

        decoded_string = decode_string(string_to_decode)

        self.assertAlmostEqual(decoded_string, expected_result)

    def test_decode_json(self):
        json_to_decode = 'eyJoZWxsbyI6ICJ3b3JsZCJ9'
        expected_result = json.dumps({"hello": "world"}, indent=4, sort_keys=True).encode()

        decoded_json = decode_json(json_to_decode)

        self.assertEqual(decoded_json, expected_result)