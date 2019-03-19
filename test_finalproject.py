from unittest import TestCase

from FinalProject import deleteRow

class TestFinalproject(TestCase):

    """Test class for FinalProject class"""

    __author__= "Khushpreet Singh"

    def test_name(self):

        """Test method for name() function in the FinalProject class """

        test = deleteRow.name(self)
        self.assertEqual(test,"Row")