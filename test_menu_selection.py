import unittest
from unittest.mock import patch, MagicMock
from menu_selection import SystemMonitor

class TestSystemMonitor(unittest.TestCase):

    @patch('psutil.disk_usage')
    def test_check_disk_usage_below_threshold(self, mock_disk_usage):
        mock_disk_usage.return_value.percent = 15
        result = SystemMonitor.check_disk_usage()
        self.assertTrue(result)

    @patch('psutil.disk_usage')
    def test_check_disk_usage_above_threshold(self, mock_disk_usage):
        mock_disk_usage.return_value.percent = 25
        result = SystemMonitor.check_disk_usage()
        self.assertFalse(result)

    @patch('psutil.cpu_percent')
    def test_check_cpu_utilization_below_threshold(self, mock_cpu_percent):
        mock_cpu_percent.return_value = 70
        result = SystemMonitor.check_cpu_utilization()
        self.assertTrue(result)

    @patch('psutil.cpu_percent')
    def test_check_cpu_utilization_above_threshold(self, mock_cpu_percent):
        mock_cpu_percent.return_value = 80
        result = SystemMonitor.check_cpu_utilization()
        self.assertFalse(result)

    @patch('psutil.net_if_addrs')
    def test_check_localhost_availability(self, mock_net_if_addrs):
        mock_net_if_addrs.return_value = {'lo': MagicMock()}
        result = SystemMonitor.check_localhost_availability()
        self.assertTrue(result)

    @patch('requests.get')
    def test_check_internet_availability_with_connection(self, mock_requests_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_requests_get.return_value = mock_response
        result = SystemMonitor.check_internet_availability()
        self.assertTrue(result)

    @patch('requests.get', side_effect=requests.ConnectionError)
    def test_check_internet_availability_without_connection(self, mock_requests_get):
        result = SystemMonitor.check_internet_availability()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
