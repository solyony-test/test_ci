from django.test import TestCase

class TestsCases(TestCase):

    def test_pass(self):
        self.assertTrue(False)
    
    def test_fail(self):
        self.assertTrue(True)
