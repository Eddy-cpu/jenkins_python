import unittest

class test_menu_selection(unittest.TestCase):
  def test_msg(self):
    a = 'Pass'
    b = 'Fail'
    self.assertEqual(a,b)

if __name__ == '__main__':
  unittest.main()
