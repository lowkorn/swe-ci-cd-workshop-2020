import unittest
from app.utility.validator import validate_name, validate_id, validate_phone_number


class TestUtility(unittest.TestCase):
    def test_validate_name_with_valid_input(self):
        self.assertEqual(True, validate_name("hanif"))

    def test_validate_name_with_invalid_input_string_of_int(self):
        self.assertEqual(False, validate_name("12312121"))

    def test_validate_id_with_valid_input(self):
        self.assertEqual(True, validate_id("1234567890987"))

    def test_validate_id_with_invalid_input_fill_out_incomplete(self):
        self.assertEqual(False, validate_id("1234567890"))

    def test_validate_id_with_invalid_input_fill_out_exceed(self):
        self.assertEqual(False, validate_id("123456789098765"))

    def test_validate_phone_number_with_valid_input(self):
        self.assertEqual(True, validate_phone_number("0812345678"))

    def test_validate_phone_number_with_valid_input_fill_out_exceed(self):
        self.assertEqual(False, validate_phone_number("08123456780"))

    def test_validate_phone_number_with_valid_input_fill_incomplete(self):
        self.assertEqual(False, validate_phone_number("0812345"))

    def test_validate_phone_number_with_valid_input_not_begin_with_zero(self):
        self.assertEqual(False, validate_phone_number("8123456780"))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
