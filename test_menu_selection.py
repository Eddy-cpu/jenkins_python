import unittest
from menu_selection.py import check_disk_usage

class TestMenuSelection(unittest.TestCase):

    def check_disk_usage(self):
        # Test case for your_menu_function1
        result = check_disk_usage()  # Replace with the actual function call
        self.assertEqual(result, "Pass", "Error: Test case 1 failed")
        
if __name__ == '__main__':
    unittest.main()
