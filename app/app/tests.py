"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """Test the calc module"""
    
    def test_add_numbers(self):
        res = calc.add(1,1)
        
        self.assertEqual(res, 2)
        
    def test_subtract_number(self):
        res = calc.subtract(10,2)
        
        self.assertEqual(res,8)
        