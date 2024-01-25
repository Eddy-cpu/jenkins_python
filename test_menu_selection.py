import unittest
from jenkins_python/menu_selection import check_disk_usage  # Import the functions you want to test from menu_selection.py

class TestMenuSelection(unittest.TestCase):

    def check_disk_usage(self):
        # Test case for your_menu_function1
        result = check_disk_usage()  # Replace with the actual function call
        self.assertEqual(result, "Pass", "Error: Test case 1 failed")  # Replace expected_result1 with the expected output
        
if __name__ == '__main__':
    unittest.main()
