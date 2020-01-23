import unittest

from name_function import get_formatted_name

# 类名可以随便起,但是必须继承TestCase类
class NamesTestCase(unittest.TestCase):
	"""测试name_function.py"""
	def test_first_last_name(self):
		formatted_name = get_formatted_name('kobe', 'blyent')
		self.assertEqual(formatted_name, 'Kobe Blyent')

unittest.main()