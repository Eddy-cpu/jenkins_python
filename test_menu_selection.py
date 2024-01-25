import unittest
from unittest.mock import patch
from menu_selection import SystemMonitor

class TestMenuSelection(unittest.TestCase):
    @patch('psutil.disk_usage')
    def test_check_disk_usage(self, mock_disk_usage):
        mock_disk_usage.return_value.percent = 25
        monitor = SystemMonitor()
        self.assertTrue(monitor.check_disk_usage())
        
    @patch('psutil.cpu_utilization')
    def test_check_cpu_utilization(self, mock_cpu_utilization):
        mock_cpu_utilization.return_value.percent = 80
        monitor = SystemMonitor()
        self.assertTrue(monitor.check_cpu_utilization())
        
    @patch('psutil.cpu_usage')
    def test_check_cpu_usage(self, mock_cpu_usage):
        mock_cpu_usage.return_value.percent = 25
        monitor = SystemMonitor()
        self.assertTrue(monitor.check_cpu_usage())
        
if __name__ == '__main__':
    unittest.main()
