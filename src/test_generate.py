import unittest

from generate import *

class TestHTMLNode(unittest.TestCase):

    # extract title
    def test_extract_title1(self):
        markdown= '''# Heading 1   

- random text 1
- random text 2
- random text 3
'''
        extracted = extract_title(markdown)
        self.assertEqual(extracted, "Heading 1")

    def test_extract_title2(self):
        markdown= ''' # Heading 1   

- random text 1
- random text 2
- random text 3
'''
        extracted = extract_title(markdown)
        self.assertEqual(extracted, "Heading 1")


    def test_extract_title2(self):
        markdown= "# Heading 1"
        extracted = extract_title(markdown)
        self.assertEqual(extracted, "Heading 1")