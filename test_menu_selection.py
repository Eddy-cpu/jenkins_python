import unittest
from unittest.mock import patch
from menu_selection import SystemMonitor

class TestMenuSelection(unittest.TestCase):
    @patch('check_disk_usage')
    def test_check_disk_usage(self, mock_disk_usage):
        mock_disk_usage.return_value.percent = 25
        self.assertEqual("Pass", "Error: Test case 1 failed")
        
if __name__ == '__main__':
    unittest.main()
