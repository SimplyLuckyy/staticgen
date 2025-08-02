import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_noteq2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is an another text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_equrl(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://https://www.wikipedia.org/")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://https://www.wikipedia.org/")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://https://www.wikipedia.org/")
        self.assertEqual(
            "TextNode(This is a text node, text, https://https://www.wikipedia.org/)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()