import unittest
from app.models import Post

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_post = Post(id=6,post='My pitch',user_id= 2)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))
