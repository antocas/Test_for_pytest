import unittest
from unittest.mock import MagicMock, patch

import addition

class TestAdd(unittest.TestCase):
	def test_addition(self):
		addit = addition.add(1, 1)
		assert addit == 2
